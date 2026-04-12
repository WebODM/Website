#!/usr/bin/env python3
"""
Download gallery screenshots and generate thumbnails.

Reads data/gallery.json, downloads full-resolution images,
generates 400px-wide thumbnails, and writes data/_gallery.json
containing only successfully processed entries.

Requirements: pip install Pillow requests
"""

import hashlib
import json
import sys
from pathlib import Path
from urllib.parse import urlparse

try:
    import requests
    from PIL import Image
except ImportError:
    print("Error: Install dependencies first: pip install Pillow requests")
    sys.exit(1)

ROOT_DIR = Path(__file__).parent.parent
GALLERY_JSON = ROOT_DIR / "data" / "gallery.json"
BUILT_JSON = ROOT_DIR / "data" / "_gallery.json"
FULL_DIR = ROOT_DIR / "static" / "images" / "gallery" / "full"
THUMB_DIR = ROOT_DIR / "static" / "images" / "gallery" / "thumbs"
THUMB_WIDTH = 400
REQUEST_TIMEOUT = 30


def url_to_filename(url: str) -> str:
    """Generate a deterministic filename from a URL, preserving the extension."""
    parsed = urlparse(url)
    ext = Path(parsed.path).suffix.lower()
    if ext not in (".png", ".jpg", ".jpeg", ".webp", ".gif"):
        ext = ".jpg"
    url_hash = hashlib.sha256(url.encode()).hexdigest()[:16]
    return f"{url_hash}{ext}"


def download_image(url: str, dest: Path) -> bool:
    """Download an image from url to dest. Returns True on success."""
    try:
        resp = requests.get(url, timeout=REQUEST_TIMEOUT, stream=True)
        resp.raise_for_status()

        with open(dest, "wb") as f:
            for chunk in resp.iter_content(chunk_size=8192):
                f.write(chunk)
        return True
    except requests.RequestException as e:
        print(f"  WARNING: Failed to download {url}: {e}")
        return False


def make_thumbnail(src: Path, dest: Path) -> bool:
    """Create a thumbnail with THUMB_WIDTH, preserving aspect ratio."""
    try:
        with Image.open(src) as img:
            if img.mode in ("RGBA", "P"):
                img = img.convert("RGB")
            ratio = THUMB_WIDTH / img.width
            new_height = int(img.height * ratio)
            thumb = img.resize((THUMB_WIDTH, new_height), Image.LANCZOS)
            thumb.save(dest, quality=85, optimize=True)
        return True
    except Exception as e:
        print(f"  WARNING: Failed to generate thumbnail for {src}: {e}")
        return False


def main():
    if not GALLERY_JSON.exists():
        print(f"Error: {GALLERY_JSON} not found")
        sys.exit(1)

    with open(GALLERY_JSON) as f:
        entries = json.load(f)

    FULL_DIR.mkdir(parents=True, exist_ok=True)
    THUMB_DIR.mkdir(parents=True, exist_ok=True)

    built = []
    total = len(entries)

    for i, entry in enumerate(entries, 1):
        url = entry.get("url", "")
        if not url:
            print(f"  [{i}/{total}] WARNING: Entry missing 'url', skipping")
            continue

        author = entry.get("author", "Anonymous")
        title = entry.get("title", "")

        filename = url_to_filename(url)
        full_path = FULL_DIR / filename
        thumb_path = THUMB_DIR / filename

        print(f"  [{i}/{total}] Processing: {url}")

        # Download full-res if not already cached
        if full_path.exists():
            print(f"    Cached: {full_path}")
        else:
            if not download_image(url, full_path):
                continue

        # Generate thumbnail if not already cached
        if thumb_path.exists():
            print(f"    Thumbnail cached: {thumb_path}")
        else:
            if not make_thumbnail(full_path, thumb_path):
                # Clean up the full image if thumbnail fails
                full_path.unlink(missing_ok=True)
                continue

        built.append({
            "full": f"/images/gallery/full/{filename}",
            "thumb": f"/images/gallery/thumbs/{filename}",
            "author": author,
            "title": title,
        })

    with open(BUILT_JSON, "w") as f:
        json.dump(built, f, indent=2)

    print(f"\nDone: {len(built)}/{total} screenshots processed successfully.")
    if len(built) < total:
        print(f"  {total - len(built)} entries skipped due to errors (see warnings above).")


if __name__ == "__main__":
    main()
