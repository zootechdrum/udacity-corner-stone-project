
export DATABASE_URL='postgresql://claireperacchio@localhost:5432/capstone'
export AUTH0_CLIENT_ID='tQtZK49lU42FD6sRTFFnxOvn7BpvINAi'
export AUTH0_DOMAIN='fsnd79.auth0.com'
export AUTH0_AUDIENCE='casting'
export AUTH0_CALLBACK_URL='http://localhost:5000/'
export ENV='development'
export FLASK_APP=app
export FLASK_DEBUG=True
export ALGORITHMS=['RS256']
export AUTH0_CLIENT_SECRET='E5ptdSiVRlPluuhWFfDfnRKAgHQchRCHU9AXuVfq75iDD45NuQFXob3DwZmkqG0x'

pip3 install -r requirements.txt

auth_token = "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlBxT0lFeU5nOEk5c2hHVG1KR2JDOSJ9.eyJpc3MiOiJodHRwczovL3pvb3RlY2hkcnVtLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw2MDQ1YTg1NDBkOWY3MTAwNzBlZTc5ODEiLCJhdWQiOlsiY29mZmUiLCJodHRwczovL3pvb3RlY2hkcnVtLnVzLmF1dGgwLmNvbS91c2VyaW5mbyJdLCJpYXQiOjE2MjA1MzE1MDgsImV4cCI6MTYyMDYxNzkwOCwiYXpwIjoiQncxNWJTNjIxNVdjaWhyRUkwOXdWVm51RjJydDhhUUgiLCJzY29wZSI6Im9wZW5pZCBwcm9maWxlIGVtYWlsIiwicGVybWlzc2lvbnMiOlsiZGVsZXRlOmFjdG9yIiwiZGVsZXRlOm1vdmllIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvciIsInBhdGNoOm1vdmllIiwicG9zdDphY3RvciIsInBvc3Q6bW92aWUiXX0.DFc0mLTHrYi_6piombd08htR-bVB0tI8oMVCVDeT21fdn9vzNGXqEg6dLlGAKcQ0AHPpGLL_77R-a02n1Xhazf4WyrGCACPLaHB3DEPXDOyw-ufexOQrcOJr7sTPBj1_Nyk7W43C0Cu13GBFBD90uQICQQMX16UWYA9_n0D_VJ7350XvEotg_-I0AiZh4Y9bbdjlqaSMicw0uqwpatSXTRCX2bqxLlma7GPtf5Dslv769s0RL4jkeQk8fWuwwZJj4x2f8z15D-TA2dcCcylzIgrcs-1F6bG5G8vcZBaV8pEr5JbiJnfNMzx5hGuXyLvAO0Jp4gGFL2s9I2zLuQM9ig"
asst_token = "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IlBxT0lFeU5nOEk5c2hHVG1KR2JDOSJ9.eyJpc3MiOiJodHRwczovL3pvb3RlY2hkcnVtLnVzLmF1dGgwLmNvbS8iLCJzdWIiOiJnb29nbGUtb2F1dGgyfDEwNDQ2MDUwMzYyNTYyMjA3MTQxMyIsImF1ZCI6WyJjb2ZmZSIsImh0dHBzOi8vem9vdGVjaGRydW0udXMuYXV0aDAuY29tL3VzZXJpbmZvIl0sImlhdCI6MTYyMDUzMjEwNCwiZXhwIjoxNjIwNjE4NTA0LCJhenAiOiJCdzE1YlM2MjE1V2NpaHJFSTA5d1ZWbnVGMnJ0OGFRSCIsInNjb3BlIjoib3BlbmlkIHByb2ZpbGUgZW1haWwiLCJwZXJtaXNzaW9ucyI6WyJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyJdfQ.ojK7yIy4IprnpTIhw-iDBHAluj1Jwgo3b3mQcyrNAGc2tkGlyWh_dvvcC_BRffbRzHf_CHHUs2xg712RETBLfpTPHutoFDnaTWVEYI3KkBFIAjqo97r2mGY-vK8LLDQ1xMaHRsOncBsxvqG1k82eJfBH6jm3s_Q8h4NN7NLZ0yGDPxDSJVHu-MNs4nqVPpW7G_Wbialto3s_Nv0f3akksJGaimBiXTAy7YPEb6bn5hAUbiuPkeVZmGlOxl008nRSVfVuoxruZoYZTbjr1S-lg4UHhPqDj_WjonK8PnAIog7jBWonlgekWKRlSthurZhAlGgaLWNsWtYn-istIe9Y8g"