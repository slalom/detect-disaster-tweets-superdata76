# detect-disaster-tweets-superdata76

# Getting Started
main.py / test_main.py are deprecated.

Jupyter uses notebook files that are executed in a browser, these are saved under `./jupyter`.
## Dependencies
docker

## Docker Build/Run Container
`docker image build -t superdata76:latest .`

Copies `./data/` and `./jupyter/` into container

`docker container run -p 8888:8888 -p 4040:4040 superdata76:latest`

```
detect-disaster-tweets-superdata76 $ docker container run -p 8888:8888 -p 4040:4040 superdata76:latest
[I 01:10:25.572 NotebookApp] Writing notebook server cookie secret to /home/jovyan/.local/share/jupyter/runtime/notebook_cookie_secret
[I 01:10:25.853 NotebookApp] Serving notebooks from local directory: /home/jovyan
[I 01:10:25.853 NotebookApp] The Jupyter Notebook is running at:
[I 01:10:25.853 NotebookApp] http://(92077ba33bd8 or 127.0.0.1):8888/?token=ce31ebdfbe453cb710d1a678ef7906fbc27addd68c961918
[I 01:10:25.853 NotebookApp] Use Control-C to stop this server and shut down all kernels (twice to skip confirmation).
[W 01:10:25.857 NotebookApp] No web browser found: could not locate runnable browser.
[C 01:10:25.858 NotebookApp] 
    
    To access the notebook, open this file in a browser:
        file:///home/jovyan/.local/share/jupyter/runtime/nbserver-1-open.html
    Or copy and paste one of these URLs:
        http://(92077ba33bd8 or 127.0.0.1):8888/?token=ce31ebdfbe453cb710d1a678ef7906fbc27addd68c961918
```

Copy token value, e.g. `ce31ebdfbe453cb710d1a678ef7906fbc27addd68c961918`, and open browser to http://127.0.0.1:8888/ and paste token to authenticate.

## Jupyter notebook
### Save notebook workflow
Because Jupyter is running on Docker in an ephemeral state, I follow this workflow to save changes to notebooks:
https://stackoverflow.com/questions/41110338/how-to-save-a-file-into-a-directory-in-jupyter-notebook
> You can save a notebook to a location of your choice by using the "File" -> "Download as" -> "Notebook (.ipynb)" option from the menu.

After saving the notebook in `./jupyter/*.ipynb`, stop Docker container, run the build step and start the container. Your updated notebook should now be available in the updated container.

### jupyter/superdata76.ipynb
http://127.0.0.1:8888/notebooks/jupyter/superdata76.ipynb

Warning: this can take several minutes to execute; it only iterates over 20 tweets, but downloading Spark dependencies can take a few minutes.

This runs an example string and tweets through `analyze_sentiment` pipeline from https://nlp.johnsnowlabs.com/docs/en/pipelines
