from visuanalytics.analytics.control.procedures.step_data import StepData
from visuanalytics.analytics.processing.image.pillow.overlay import OVERLAY_TYPES
from visuanalytics.analytics.util import resources
from PIL import Image
from PIL import ImageDraw


def generate_image_pillow(values: dict, prev_path, presets: dict, step_data: StepData):
    if values.get("edit-prev-image", False):
        source_img = Image.open(resources.get_resource_path(prev_path))
    else:
        source_img = Image.open(resources.get_resource_path(values["path"]))
    img1 = Image.new("RGBA", source_img.size)
    draw = ImageDraw.Draw(source_img)
    for overlay in values["overlay"]:
        OVERLAY_TYPES[overlay["type"]](overlay, source_img, draw, presets, step_data)
    file = resources.new_temp_resource_path(step_data.data["_pipe_id"], "png")
    Image.composite(img1, source_img, img1).save(file)
    return file
