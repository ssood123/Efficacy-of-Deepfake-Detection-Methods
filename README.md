# Efficacy-of-Deepfake-Detection-Methods

### HeavyweightFaceswapImagesAndVideos

This folder contains 3 subfolders. HeavyweightFaceswapImages stores heavyweight faceswap images/frames extracted from the heavyweight faceswap video dataset on Zenodo. HeavyweightFaceswapImagesFACE contains images of the zoomed-in faces of the images from the HeavyweightFaceswapImages folder. HeavyweightFaceswapVideosFACE contains videos created from the frames in the HeavyweightFaceswapImagesFACE folder.

### LightweightFaceswapImagesAndVideos

This folder contains 3 subfolders. LightweightFaceswapImages stores lightweight faceswap images/frames extracted from the lightweight faceswap video dataset on Zenodo. LightweightFaceswapImagesFACE contains images of the zoomed-in faces of the images from the LightweightFaceswapImages folder. LightweightFaceswapVideosFACE contains videos created from the frames in the LightweightFaceswapImagesFACE folder.

### Face2FaceImagesAndVideos

This folder contains 3 subfolders. Face2FaceImages stores face2face images/frames extracted from the face2face video dataset on Zenodo. Face2FaceImagesFACE contains images of the zoomed-in faces of the images from the Face2FaceImages folder. Face2FaceVideosFACE contains videos created from the frames in the Face2faceImagesFACE folder.

### RealImagesAndVideos

This folder contains 3 subfolders. RealImages stores real/unmodified images/frames extracted from the original video dataset on Zenodo. RealImagesFACE contains images of the zoomed-in faces of the images from the RealImages folder. RealVideosFACE contains videos created from the frames in the RealImagesFACE folder.

### ArtificiallyGeneratedFaceImagesAndVideos

This folder contains 2 subfolders. ArtificiallyGeneratedFaceImages contains images downloaded directly from https://this-person-does-not-exist.com/en. ArtificiallyGeneratedFaceVideos contains videos created the frames in the ArtificiallyGeneratedFaceImages folder.

### StyleGANImages

This folder contains 10 subfolders. Each subfolder represents an imageset of 600 videos each. Each imageset consists of StyleGAN-generated faces of people with particular facial expressions or features. For example, AngryImages contains 600 images of people with angry expressions and LongHairImages contains 600 images of people with long hair.

### MesoNet

This folder consists of the data and scripts needed to run MesoNet. In addition to Mesonet.ipynb and the weights folder, one needs to craete a folder named "data" consisting of all the images that need to be classified. When Mesonet.ipynb is run, it will classify all images in the "data" folder and organize the results into 3 meaningful tables after.

### DeepwareAI

The original repo can be found here: https://github.com/deepware/deepfake-scanner. This folder consists of the data and scripts needed to run DeepwareAI. In addtion to the files already stored already stored in this folder, one needs to create a folder named "weights" that contains the weights that can be downloaded from https://github.com/deepware/deepfake-scanner. One also needs to create a folder named "videos" that contains that videos to be classified by DeepwareAI. After, DeepwareAI.ipynb needs to be run, after which DeepwareAI will generate a results.csv file consisting of its predictions for each video in the "videos" folder. Finally, analyzeDeepwareCSVdata.ipynb needs to be run to generate meaningful table data from results.csv.
