# abalyzer

I needed to interpret the result of A/B tests in the most straightforward possible way, and I found that `statsmodels` added half a GB to our Docker images.
Given I only need to do that once a week or so, it didn't make sense at all, so decided to deploy what I needed as an AWS Lambda.

Not much here, besides the few tests I wanted and the basic Dockerfile I needed - Lambda setup is left to the reader.
