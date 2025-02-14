import os
import pathlib
from deepinterpolation.cli.training import Training

if __name__ == '__main__':
    # Initialize meta-parameters objects
    training_param = {}
    generator_param = {}
    network_param = {}
    generator_test_param = {}

    # An epoch is defined as the number of batches pulled from the dataset.
    # Because our datasets are VERY large. Often, we cannot
    # go through the entirity of the data so we define an epoch slightly
    # differently than is usual.
    steps_per_epoch = 5

    # Those are parameters used for the Validation test generator.
    # Here the test is done on the beginning of the data but
    # this can be a separate file
    generator_test_param["name"] = "SingleTifGenerator"
    # Name of object in the collection
    generator_test_param[
        "pre_post_frame"
    ] = 30  # Number of frame provided before and after the predicted frame
    generator_test_param["train_path"] = os.path.join(
        pathlib.Path(__file__).parent.absolute(),
        "..",
        "sample_data",
        "ophys_tiny_761605196.tif",
    )
    generator_test_param["batch_size"] = 5
    generator_test_param["start_frame"] = 0
    generator_test_param["end_frame"] = 100
    generator_test_param[
        "pre_post_omission"
    ] = 1  # Number of frame omitted before and after the predicted frame
    generator_test_param["steps_per_epoch"] = -1
    # No step necessary for testing as epochs are not relevant.
    # -1 deactivate it.

    # Those are parameters used for the main data generator
    generator_param["steps_per_epoch"] = steps_per_epoch
    generator_param["name"] = "SingleTifGenerator"
    generator_param["pre_post_frame"] = 30
    generator_param["train_path"] = os.path.join(
        pathlib.Path(__file__).parent.absolute(),
        "..",
        "sample_data",
        "ophys_tiny_761605196.tif",
    )
    generator_param["batch_size"] = 5
    generator_param["start_frame"] = 0
    generator_param["end_frame"] = 100
    generator_param["pre_post_omission"] = 0

    # Those are parameters used for the network topology
    network_param["name"] = "unet_single_1024"
    # Name of network topology in the collection

    # Those are parameters used for the training process
    training_param["name"] = "core_trainer"
    training_param["learning_rate"] = 0.0001
    training_param["loss"] = "mean_squared_error"
    training_param["output_dir"] = str(pathlib.Path(__file__)
                                       .parent.absolute())

    training_param["model_string"] = (
        network_param["name"]
        + "_"
        + training_param["loss"]
    )

    args = {
        "training_params": training_param,
        "generator_params": generator_param,
        "test_generator_params": generator_test_param,
        "network_params": network_param,
        "output_full_args": True
    }

    trainer = Training(input_data=args, args=[])
    trainer.run()
