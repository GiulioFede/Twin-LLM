# Twin-LLM
An LLM that is your twin


#FTI (Feature, Training, Inference)
Per evitare di avere un codice monolitico che gestisce tutto, un complesso ML system viene progettato secondo il pattern Feature, Training, Inference (FTI). Ovvero dai raw data vengono estratte le feature e le etichette (Feature stage) e vengono salvate in un feature store, poi si allena il modello con le feature e salvato in un model registry (Training stage) e infine si procede con l'inferenza usando le feature nuove + feature estratte e modello allenato (Inference stage).