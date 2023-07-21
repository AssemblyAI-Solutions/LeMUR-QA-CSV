# LeMUR-QA-CSV

### Getting Started

Step 1: Clone repo to local directory

Step 2: Activate python virtual enviroment
```
python3 -m venv venv
    
source venv/bin/activate
```

Step 3: Install requirements
```
pip install -r requirements.txt
```
Step 5: Set AssemblyAI API Key
```
export ASSEMBLYAI_API_TOKEN=<API KEY HERE>
```

Step 6: Update ```questions.py``` with LeMUR Questions

Step 7: Update ```audio_url.json``` with Audio URLs to process

Step 8: Run ```python3 app.py```

Step 9: View ```output.csv```
