# ComfyUI Optional Image Gate

A minimal ComfyUI custom node that switches an optional reference-image input
between an actual `IMAGE` value and a real empty Python list (`[]`).

This is useful for API image-generation nodes that interpret an empty image
list as text-to-image mode and a non-empty image input as reference-image mode.

## Install

Copy this repository folder into:

```text
ComfyUI/custom_nodes/comfyui_optional_image_gate
```

Restart ComfyUI and refresh the browser. Search for:

```text
Optional Image Gate (Image / Empty List)
```

## Wiring

```text
Load Image --------> image
Boolean condition -> enable
images output -----> the optional images input of the generation node
```

- `enable` is a connectable `BOOLEAN` socket, not a manual toggle widget.
- `enable = true`: outputs the connected image.
- `enable = false`: outputs an empty Python list (`[]`).

The downstream node must explicitly support an empty list as “no reference
images”. Do not replace the empty list with a black, transparent, or 1×1 image;
those are still real reference images.
