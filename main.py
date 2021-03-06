import torch
import models.unet_v2 as model
import log_utils.log_tensorboard as log
from training.train import train
from training.validation import eval

# from torchvision.models.segmentation import DeepLabV3


if __name__ == "__main__":
    # Create logger
    log.init("kek_2")

    # Try to use GPU
    device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
    print(device)

    # Create an instance of the model
    net = model.Net(n_channels=3, n_classes=21)
    net.to(device)
    PATH = 'model_instances/voc_net_tmp.pth'
    net.load_state_dict(torch.load(PATH))

    # Train for some epochs
    # train(net, epoch_count=100, start_epoch=0, use_scheduler=True)
    eval(net)

    # Save our beautiful model for future generations
    # PATH = 'model_instances/voc_net_tmp.pth'
    # torch.save(net.state_dict(), PATH)
