# Scripts for Automatic1111

Scripts go in the automatic1111 stable-diffusion-webui / scripts folder.

## Prompt S/R Batch

Note: I'm afraid this is **not compatible with the "dynamic prompts" extension**, simply untick 'enable' in dynamic prompts when using this.

Generating e.g. 4 images in 1 batch is slightly faster than 4x1 image, but normally they'd all get the same prompt.

This script allows you to change the prompt for each image in one batch.

It works like the prompt s/r in xyz grid, search and replace, but, also overrides the batch setting.

So, put 'car' in the main automatic1111 prompt. Select 'Prompt S/R Batch' from the scripts drop down. 

In the textbox, put 'car, house, tree, frog' in the text box, and boom, 4 images in 1 batch, each with its own prompt.

![image](https://github.com/Luke2642/webui-scripts/assets/36384924/df79220c-1070-454f-ac57-8f305f44c9a6)
