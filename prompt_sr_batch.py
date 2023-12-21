import modules.scripts as scripts
import gradio as gr
from modules.processing import process_images, StableDiffusionProcessingTxt2Img

class PromptSRBatchScript(scripts.Script):
    def title(self):
        return "Prompt S/R Batch"

    def ui(self, is_img2img):
        if not is_img2img:
            return [gr.Textbox(label="Comma separated list. Not compatible with dynamics prompts extension, simply untick enable.", 
                               placeholder="First item to replace, followed by replacements. Example: car, house, tree, frog", 
                               lines=2)]
        return []

    def run(self, p, prompt_sr):
        # Split the input into a list, where the first item is the target string and the rest are replacements
        prompt_parts = [part.strip() for part in prompt_sr.split(',')]
        target_string = prompt_parts[0]
        replacements = prompt_parts[1:]

        # Check if the target string is in the original prompt
        if target_string not in p.prompt:
            raise ValueError(f"The string '{target_string}' was not found in the original prompt.")

        # Set the batch size to the number of replacements plus one for the original prompt
        p.batch_size = len(replacements) + 1
        p.n_iter = 1

        # Create a list of modified prompts, including the original prompt
        modified_prompts = [p.prompt] + [p.prompt.replace(target_string, replacement) for replacement in replacements]

        # Process the images with modified prompts
        p.prompt = modified_prompts
        processed_results = process_images(p)

        # Return the results
        return processed_results

