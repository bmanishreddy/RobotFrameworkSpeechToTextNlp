Make sure you install the following packages in your system 
pip install speech_recognition 
pip install spacy


place this perticular package under your site-packages 


Example request that you can make to the library 


###    code

,,,
*** Settings ***
Test Timeout      15 minutes
Resource          Resource.txt

*** Test Cases ***
InitialRequest
    [Tags]    ServiceTest
    ${CE}    Voice Conv    Conv2.wav
    log    ${CE}
    ${CE}    Extract Info Noun Chunks    Conv2.wav
    log    ${CE}
    ${CE}    Lemma    Conv2.wav
    log    ${CE}
    ${CE}    Parts Of Speech    Conv2.wav
    log    ${CE}

,,,

Result wiould be somethig like this :- 


