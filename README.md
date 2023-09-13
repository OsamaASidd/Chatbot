
# AI
It's just a simple AI using OpenAI GPT-3 and flask (Python)  

## Setup

1. Install Docker Desktop

2. Build Dockerfile 

  ```bash
   $ docker build -t my-app .      
   ```

3. Run Dockerfile

```bash
   $ docker run -p 5000:5000 my-app    
   ```


## Customize

You can change your AI, you need to change the `conversation` and add or delete what you want to be your real AI

You can update the picture on main.css ` <img src="{{ url_for('static', filename='download.png') }}" >`
 

![OpenAI](https://i.blogs.es/0dbd39/openai-gpt-3/1366_2000.jpg)

## Authors

- [@OsamaASidd](https://github.com/OsamaASidd)

