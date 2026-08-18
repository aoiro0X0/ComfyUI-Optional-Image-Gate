class OptionalImageGate:
    """Pass an IMAGE through when enabled; otherwise pass an empty image list."""

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "image": ("IMAGE",),
                "enable": ("BOOLEAN", {"default": False, "forceInput": True}),
            }
        }

    RETURN_TYPES = ("IMAGE",)
    RETURN_NAMES = ("images",)
    FUNCTION = "gate"
    CATEGORY = "ByteArtist/logic"

    def gate(self, image, enable):
        if enable:
            return (image,)
        return ([],)


NODE_CLASS_MAPPINGS = {
    "OptionalImageGate": OptionalImageGate,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "OptionalImageGate": "Optional Image Gate (Image / Empty List)",
}
