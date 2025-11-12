import time

class SequentialImageSelector:
    """
    Sequentially selects one of up to six input images.
    On each new execution, it advances to the next connected image.
    """

    last_index = -1  # persists across executions (class-level variable)

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "optional": {
                "image1": ("IMAGE",),
                "image2": ("IMAGE",),
                "image3": ("IMAGE",),
                "image4": ("IMAGE",),
                "image5": ("IMAGE",),
                "image6": ("IMAGE",),
            }
        }

    RETURN_TYPES = ("IMAGE", "INT")
    RETURN_NAMES = ("selected_image", "index")
    FUNCTION = "select_next"
    CATEGORY = "image/sequence"

    @classmethod
    def IS_CHANGED(cls, **kwargs):
        # Ensures ComfyUI re-runs the node each queue
        return float(time.time())

    def select_next(self, image1=None, image2=None, image3=None, image4=None, image5=None, image6=None):
        # Collect connected images
        images = [img for img in [image1, image2, image3, image4, image5, image6] if img is not None]
        if not images:
            raise ValueError("No image inputs connected")

        # Move to next index cyclically
        SequentialImageSelector.last_index = (SequentialImageSelector.last_index + 1) % len(images)
        selected_index = SequentialImageSelector.last_index
        selected_image = images[selected_index]

        print(f"[SequentialImageSelector] Loaded image {selected_index + 1}/{len(images)}")
        return (selected_image, selected_index)


NODE_CLASS_MAPPINGS = {"SequentialImageSelector": SequentialImageSelector}
NODE_DISPLAY_NAME_MAPPINGS = {"SequentialImageSelector": "Sequential Image Loader 🔁"}
