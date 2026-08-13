+++
title = "ODX"
description = "ODX is a free and open source photogrammetry engine for processing aerial and ground imagery. It turns images into point clouds, 3D models, orthophotos and elevation models."
+++

# ODX

A free and open source photogrammetry engine for processing aerial and ground imagery. ODX turns images into:

* Classified Point Clouds
* 3D Textured Models
* Georeferenced Orthophotos
* Georeferenced Digital Elevation Models

![ODX Pipeline](https://user-images.githubusercontent.com/1174901/96613039-7de94500-12cc-11eb-9975-ca67b188b0d3.png)

The application is available for Windows, Mac and Linux and it works from the command line, making it ideal for power users, scripts and for integration with other software.

### Windows

First download the latest [Windows setup](https://github.com/WebODM/ODX/releases). After installation, open the `ODX Console`, place some images in a folder named `images` (for example `C:\Users\youruser\datasets\project\images`) and run:

```bash
run c:\Users\youruser\datasets\project
```

Alternatively, you can also use [docker](https://docs.docker.com):

```bash
# Windows
docker run -ti --rm -v c:/Users/youruser/datasets:/datasets webodm/odx --project-path /datasets project
```

### macOS/Linux

First install [docker](https://docs.docker.com). Once you have docker installed, place some images in a folder named `images` (for example `C:\Users\youruser\datasets\project\images` or `/home/youruser/datasets/project/images`) and run from a terminal:

```bash
# Mac/Linux
docker run -ti --rm -v /home/youruser/datasets:/datasets webodm/odx --project-path /datasets project
```

## Arguments

You can pass [additional parameters](https://docs.webodm.org/options-flags/) by appending them to the command:

```bash
run c:\Users\youruser\datasets\project [--args]
```

```bash
docker run -ti --rm -v /datasets:/datasets webodm/odx --project-path /datasets project [--args]
```

For example, to generate a DSM (`--dsm`) and increase the orthophoto resolution (`--orthophoto-resolution 2`) :

```bash
docker run -ti --rm -v /datasets:/datasets webodm/odx --project-path /datasets project --dsm --orthophoto-resolution 2
```

To see all parameters:

```bash
docker run -ti --rm -v /datasets:/datasets webodm/odx --help
```

<div class="text-center mt-5">
  <a href="https://github.com/WebODM/ODX" class="btn btn-primary btn-lg">
    <i class="bi bi-github me-2"></i>ODX on GitHub
  </a>
</div>


