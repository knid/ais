
<h2 align="center">
<img height="150" src="https://raw.githubusercontent.com/knid/ais/master/docs/icon.png" />
    <br>
<br>
- AIS -
</h2>


<div align="center">
<!---
<a href="https://www.buymeacoffee.com/knid"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png"/></a>
-->
</div>


Ais (ai shell) is interactive command line ai tool powered by ChatGPT (GPT-3.5). Ais can translate your query into a bash command and explain it to you if you want. In this way, you can get rid of hours of searching for small tasks and increase your learning spectrum.

<img src="https://github.com/knid/ais/blob/master/docs/ais.gif?raw=true" alt="ais in action" width="100%">


## Getting started

### Installation instructions
(require python3.6+)


```bash
pip install ais-cli
```


### Setup
Setup open ai access key
```bash
ais set ACCESS_KEY <KEY>
```

## Running queryies

### Turn to command
You can just write the what do you want. It will be turn a bash command

```bash
ais • open rtsp::113.76.151.33/1 with ffplay without sound
──────────────  Command  ───────────────────

ffplay -an rtsp://113.76.151.33/1

? Select action (Use arrow keys)
 ◌ ✅ Run this command
   ❔ Explain this command
   ❌ Cancel
```

### Explain commands
If you select "Explain this command" action ChatCGT will explain this command for you.

```bash
? Select action (Use arrow keys)
 ◌ ✅ Run this command
   ❔ Explain this command
   ❌ Cancel
```
<!-- ```bash -->
<!-- ais • make 2x faster video.mp4 -->
<!-- ──────────────────  Command  ─────────────────── -->
<!---->
<!-- ffmpeg -i video.mp4 -filter:v "setpts=0.5*PTS" -an output.mp4 -->
<!---->
<!-- ? Select action ❔ Explain this command -->
<!---->
<!-- ──────────────────  Explain  ──────────────────── -->
<!---->
<!-- This is a command for using ffmpeg to manipulate a video file  -->
<!-- called "video.mp4". The "-filter:v" option is used to apply a video filter, -->
<!-- in this case "setpts=0.5*PTS", which will change the playback speed of the video. -->
<!-- The resulting video will have no audio, as indicated  -->
<!-- by the "-an" option. The output file will be called "output.mp4". -->
<!-- ``` -->

### Regular questions
Run `ais ask` for asking normal questions.

```bash
ais • ais ask how are you?
───────────  Result  ─────────────

I am an AI language model, so I do not have feelings or emotions.
But thank you for asking! How may I assist you today?
```

### Run system command in interactive mode
Use the `!` character as the first character
```bash
ais • !whoami

knid
```

### Run without interactive mode

#### Create bash script
```bash
ais -c "create port scanner with bash"
```
#### Ask regular questions
```bash
ais -c "ais ask Who is Ataturk"
```
