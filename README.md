<div align="center">
<img src="https://res.cloudinary.com/canonical/image/fetch/f_auto,q_auto,fl_sanitize,c_fill,w_1440/https://ubuntu.com/wp-content/uploads/c9f4/visualstudio_code-card.png" width="200px">

A Lightning component to Launch Visual Studio Code Server
______________________________________________________________________
</div>

### [Visual Studio Code Server](https://github.com/coder/code-server)

In VS Code, users can seamlessly leverage the environments that make them the most productive. This component will install Visual Studio Code Server within a `Work` with a compute profile of your choice and access it in a browser.

![VSCode](images/vscode-ss.png)

### Usage


```
from lit_vscode import VSCodeServer
import lightning as L
import os

class RootFlow(L.LightningFlow):
    def __init__(self) -> None:
        super().__init__()
        self.vscode_work = VSCodeServer(cloud_compute=L.CloudCompute(os.getenv("LIGHTNING_VSCODE_COMPUTE", "cpu-small")))

    def run(self):s
        self.vscode_work.run()
    
    def configure_layout(self):
        return [{'name': "VSCode", 'content': self.vscode_work}]

app = L.LightningApp(RootFlow())
```

By default this component launches with cpu-small [Compute](https://lightning.ai/lightning-docs/core_api/lightning_work/compute.html) Instance. This can be overridden using the LIGHTNING_VSCODE_COMPUTE environment variable.

```
lightning run app demo_app.py --cloud
lightning run app demo_app.py --cloud --env LIGHTNING_VSCODE_COMPUTE=gpu
```

### Known Issues
At this moment copy and paste to the terminal does not work. As a workaround you can paste to an existsing or a new file.

### TODO
- [ ] Unit Test
- [ ] CI Pipeline
- [ ] Precommit
