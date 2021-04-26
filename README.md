# Blue Squad Senior Data & Software Engineer Coding Challenge

## Objective
- Start by a taking a look at the image provided in the `mockups` directory of this repository. This is a mockup of a type of screen in our mobile app, showing details about an elected official (aka "representative"). Once you have reviewed this image, come back to read the rest of this README.
- Your objective is to implement a Python process that will fetch data from the Google Civic API, clean it and restructure it, and load it to a remote Mongo database. In a real-world scenario, this data would then be accessed by our internal API to serve data to our mobile app to populate this type of screen. More details about each component of this objective are below.

## Google Civic API
- You will need a Google API key in order to access the Google Civic API. Note that calls to the Google Civic API incur no cost. Instructions are found [here](https://support.google.com/googleapi/answer/6158862?hl=en) for creating a Google API key.
  - Once you create the API key, make sure it is associated with the Google API project you will be using. The first time you try to use it, you may get a response indicating it is not associated with the project; follow the link included in the response to include it.
  - Additionally, we recommend restricting this API key to only the Google Civic API, to avoid accidental or unauthorized use to cost-incurring endpoints. To restrict the API, from the Credentials screen (under APIs and services), click on the name of your API key and on the next page, under API restrictions, click "Restrict key" and then select the "Google Civic Information API" item, and click save. Unfortunately, the Google Civic Information API does not seem to show up as an option in the list until you have used the API key to access the Google Civic API at least once, so if it is not in the list, go ahead and use the API key to make a request to the Google Civic API (you may want to read the rest of this section first), then return to this screen to try again.
  - If you have any questions or problems with setting up your API key, please don't hesitate to reach out, as we don't want this part of the challenge to slow you down.
- The Google Civic API contains several endpoints, but the one you will be using is the `representativeInfoByDivision` endpoint, with documentation [here](https://developers.google.com/civic-information/docs/v2/representatives#resource).
  - You only need to get data for statewide representatives - that is, elected officials who represent an entire state, such as a Governor or U.S. Senator (as opposed to representatives who represent geographic areas within a state, such as members of state legislatures or city mayors).
  - Because you will be using the `representativeInfoByDivision` endpoint, you will need to provide OCD IDs as part of your requests. OCD ID stands for Open Civic Data identifier, which is a standard used to identify political geographic divisions. These identifiers follow a standard pattern: they begin with `ocd-division/` and are followed by one or more divisions, where each division is entirely geographically encompassed by the preceding division. Each division is structured `{division_type}:{division_name}`, and each division is separated by `/`. The first division is always `country:{country_code}`. For example, the OCD ID for the state of Texas is `ocd-division/country:us/state:tx`. All states are listed with their 2-letter abbreviation.
    - The information provided in this document should be sufficient for the purposes of this coding challenge, but if you are curious to learn more about OCD IDs, you can find more information [here](https://github.com/opencivicdata/ocd-division-ids/blob/master/identifiers/country-us/README.md).
- While the Google Civic API is free to use, there are rate limits in place, which are listed in an answer in [this FAQ page](https://docs.google.com/document/u/1/d/1AFIDXn53AOEkdaGlvnpB3d73fn8EgGH_PSlWlm82bcA/pub). According to these limits, you should not need to implement rate limiting in your code. However, if you do find yourself running into rate limits, or if you simply want to add a rate limiter, please feel free to add one, and feel free to keep it basic. In other words, we do not expect you to implement rate limiting for a high-volume scenario.

## Data Cleaning & Processing
- Use the mockup as a guide for how to clean and restructure the data, keeping in mind that it will ultimately be used to populate data for screens like the one in the mockup. We are intentionally not providing specific instructions here, because we want to see what you come up with. Being able to work backwards from a mockup to determine how data should be processed and stored is a key part of this role.
- When deciding how to process and structure your data, keep in mind that although we are only asking you to handle statewide representatives for this coding challenge, in a real-world scenario we would be including more local-level results as well. You can try constructing various OCD IDs (e.g. for a city or county) and looking at their responses if you like. Although you do not need to handle all edge cases for more local results, your overall data structure should take into account that there could be geographies other than statewide.
- Along similar lines, although this coding challenge does not require processing a large volume of data, your code should be written to perform efficiently, such that processing a large volume of data would still be fast. (The exception to this is rate limiting, as mentioned above.)

## MongoDB
- In the email we sent that had the link to this repo, we also provided you with the hostname of a cloud machine running Mongo, the port that Mongo is listening for connections on, a database name, and a username and password that grants you access to this database.
  - If you have any problems connecting to Mongo, please let us know.
- Only you and our team have access to this database, so feel free to use it to test out your code while you are developing. However, using this database for purposes other than this coding challenge and/or storing large quantities of data (i.e. magnitudes more than what is expected for this challenge) is not permitted.
- Store your cleaned data in a collection called `representatives`.
- As mentioned in the previous section, it is up to you to design a data model that you feel is appropriate for this objective.
- Your code should be written for a production environment in which your code will be executed repeatedly over time, to keep the `representatives` data up-to-date and accurately reflecting current representatives.

## Requirements
- Your code must be written in Python 3 (3.7 or higher).
- Feel free to use common open-source libraries, as long as they are not specific to the Google Civic API. Please use a `requirements.txt` file for all dependencies.
- Although you may use libraries, the development and content of the submission must be entirely your own. It is okay to leverage small snippets (e.g. a few lines) from library documentation or existing answers on StackOverflow.
- You are welcome to split your code into as many modules and files as you would like, but ultimately the entire process should be able to be run with one single command.
- Do NOT include your API key or any of the Mongo connection data (hostname, database name, username, and password) in your code. These should be provided as arguments to the command.
- We will be evaluating your code (including running it several times), as well as the data found in the `representatives` collection in Mongo. It does not matter whether there is data in that collection upon submission or not, but any data in it should be a reflection of your desired result.

## Submission Instructions
- Create a *private* Github repo. Feel free to name it whatever you want.
- Add everything necessary into that repo along with instructions on how to execute your code.
- When you're ready for us to take a look:
  - Share the repo via Github with Kate, Shion, and Moe - our Github accounts are under `<firstname>@bluesquad.co`
  - Email Kate to let us know the repo name and your Github username

## Additional Thoughts
- We recommend spending no more than a day working on your submission. If you find that the work is taking longer than this, it's possible that this role may not be the best fit for you.
  - If you find yourself running out of time, we prefer that you prioritize functionality over elaborate error handling or data cleaning.
- We've left these instructions to be a little vague because part of this challenge is you figuring out what to do and how to do it. That said, please don't hesitate to ask questions! We'll let you know if it's something we expect you to figure out on your own :). Good luck and we hope you have fun!
