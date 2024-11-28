import wandb
print(f"The wandb version is {wandb.__version__}")
assert wandb.__version__ == '2.19.0', f'Expected version 2.19.0, instead got {wandb.__version__}'
