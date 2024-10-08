import json

# Simulate the JSON data by copying it into a variable (this would normally be fetched from the URL)
json_data = """
{"date":"2024-08-11",
"explanation":"Where do Perseid meteors come from? Mostly small bits of stony grit, Perseideteoroids  mwere once expelled from Comet Swift-Tuttle and continue to follow this comet's orbit as they slowly disperse.  The featured animation depicts the entire meteoroid stream as it orbits our Sun.  When the Earth nears this stream, as it does every year, the Perseid Meteor Shower occurs.  Highlighted as bright in the animation, comet debris this size is usually so dim it is practically undetectable.  Only a small fraction of this debris will enter the Earth's atmosphere, heat up and disintegrate brightly.  Tonight and the next few nights promise some of the better skies to view the Perseid shower as well as other active showers because the first quarter moon will be absent from the sky from midnight onward.   Your Sky Surprise: What picture did APOD feature on your birthday? (post 1995)",
"media_type":"video",
"service_version":"v1",
"title":"Animation: Perseid Meteor Shower",
"url":"https://www.meteorshowers.org/view/perseids"
}
"""

# Load the JSON data into a Python dictionary
data = json.loads(json_data)

# Extract and print the "explanation" and "title"
explanation = data.get("explanation")
title = data.get("title")

print(f"Title: {title}")
print(f"Explanation: {explanation}")
