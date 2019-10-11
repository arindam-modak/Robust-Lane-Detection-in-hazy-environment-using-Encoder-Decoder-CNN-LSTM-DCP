import keras_segmentation

model = keras_segmentation.models.segnet.segnet(n_classes=2 ,  input_height=128, input_width=256)

model.train( 
    train_images =  "C:\\Users\\arind\\OneDrive\\Desktop\\Sem7-project\\inputimages",
    train_annotations = "C:\\Users\\arind\\OneDrive\\Desktop\\Sem7-project\\inputimages_ann",
    epochs=1
)

out = model.predict_segmentation(
    inp="C:\\Users\\arind\\OneDrive\\Desktop\\Sem7-project\\img261.png",
    out_fname="out3.png"
)

