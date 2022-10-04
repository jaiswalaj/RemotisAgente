# Remotis Agente

<br/>

## Introduction

Remotis Agente is an API built with Flask which can be used to transmit shell commands via POST requests and receive the command's output as part of the API response.

Make sure to send the appropriate command to the appropriate OS agent because shell commands are OS-specific.

<br/>

## Prerequisite
>Python 3.10.1 or above
>Pip v22.2.1 or above
>Flask

<br/>

## Launch the Agent Server

1. After locally cloning the Github repository, unzip the downloaded file.
2. Open your terminal and navigate to the unzipped folder.
3. To start the agent, enter the following commands into the terminal.
	>`pip install -r requirements.txt`
	>`python agentapp.py`

When the commands are successfully executed, you will see output that looks like the output shown below
> * Running on all addresses (0.0.0.0)
> * Running on http://127.0.0.1:80
> * Running on http://192.168.0.142:80
>Press CTRL+C to quit

<br/>

## Interacting with the Agent Server

Once the Agent Server is operational, we can use distant computers connected to the same network to issue shell commands to the Python agent using the IPs provided by the agent, and we can then get the results of those commands as API responses.

To accomplish that, we must send the shell `command` in `curl` request to the address where the agent server is running with the route `/command/`.

For example:
>curl -X POST http://192.168.0.142:80/command/ -H "Content-Type: application/x-www-form-urlencoded" -d "command=mkdir C:\Users\HP\Documents\newTestDir"

>curl -X POST http://192.168.0.142:80/command/ -H "Content-Type: application/x-www-form-urlencoded" -d "command=echo 'Hello World'"

>curl -X POST http://192.168.0.142:80/command/ -H "Content-Type: application/x-www-form-urlencoded" -d "command=ipconfig"

<br/>

## Sample Screenshots

<br/>

Sample Output #1
![Sample Output #1](./sampleOutput/sample_1.jpg)

<br/>

Sample Output #2
![Sample Output #2](./sampleOutput/sample_2.jpg)

<br/>

Sample Output #3
![Sample Output #3](./sampleOutput/sample_3.jpg)

<br/>

## License
MIT

**Is this Free, Hell Yeah!**