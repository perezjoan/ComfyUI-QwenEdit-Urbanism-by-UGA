import random
import time

class RandomImageSelector:
    """Randomly selects one of up to six input images on each execution."""

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
    FUNCTION = "select_random"
    CATEGORY = "image/random"

    # Force node to refresh on every queue
    @classmethod
    def IS_CHANGED(cls, **kwargs):
        return float(time.time())

    def select_random(self, image1=None, image2=None, image3=None, image4=None, image5=None, image6=None):
        # Gather only connected images
        images = [img for img in [image1, image2, image3, image4, image5, image6] if img is not None]
        if not images:
            raise ValueError("No image inputs connected")

        random.seed(time.time())
        selected_index = random.randint(0, len(images) - 1)
        selected_image = images[selected_index]

        print(f"[RandomImageSelector] Selected index: {selected_index}")
        return (selected_image, selected_index)


NODE_CLASS_MAPPINGS = {"RandomImageSelector": RandomImageSelector}
NODE_DISPLAY_NAME_MAPPINGS = {"RandomImageSelector": "Random Image Selector 🎲"}
