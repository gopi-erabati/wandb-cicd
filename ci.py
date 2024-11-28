import wandb
print(f"The wandb version is {wandb.__version__}")
assert wandb.__version__ == '0.18.7', f'Expected version 0.18.7, instead got {wandb.__version__}'
