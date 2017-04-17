# Wishlist for contributions

Get in touch with @sam on the [Data for Democracy](github.com/data4Democracy/read-this-first) Slack, or drop a github issue.

1. Tying article text in with full text found online. This would help us categorize the articles on the front page as well, since we would get the taxonomy from the news site, as well as having more training data for a topic model. We could also detect what words get buried behind the front page fold.

2. Combining headlines with article text. There is no logical (in database) connection between headlines, bylines, and the main bulk of an article. For certain tasks, like figuring out whether one particular candidate is getting significantly more headline-time in an article that mentions both candidates, this could be helpful. I find that at least one side of the headline bounding box tends to be aligned along the sides of the article, but I'm not sure how generalizable this is.

3. PDF extraction: Right now, text can be extracted from about half of the PDFs, and it's very skewed by newspaper. This means that we were able to extract text from all of The Denver Post, but none of The New York Times. The current approach is to use [pdfminer](https://github.com/jaepil/pdfminer3k)'s XML output, and to give up when pdfminer fails to parse a newspaper. I would like to switch to a less automated solution where we traverse the text objects ourselves, using a tool like [PyPDF2](https://github.com/mstamy2/PyPDF2).

4. Cleaning up artifacts from PDF extraction: Since pulling text from PDFs is imperfect, we often end up with words that are joined together, or split apart. I have already done some preliminary work here, with joining words that were broken up at the end of a line like this: "explora-\ntion". A quick peek in the data will reveal more examples.

5. More robust ad detection. At the moment, I'm filtering out any text boxes that appear more than once in a paper -- the idea is, actual article headlines and text are very unlikely to repeat themselves as an entire block. However, bylines, newspaper titles, etc. get caught by this. Some ads do too. It could be helpful to categorize the filtered data we have into byline, advertisements, titles, etc.

6. Image analysis. I don't pull out the images from the PDFs at the moment. It would be helpful if someone could extract images, and gather tags for them from a system like [Clarifai](https://www.clarifai.com/) (for example).
