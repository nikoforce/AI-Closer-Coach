import streamlit as st
import whisper

# Charger le modèle Whisper
model = whisper.load_model("base")

st.title("Analyse AI des Appels de Setting")

st.write("Téléverse ton fichier audio ou texte pour commencer.")

# Téléchargement du fichier (texte ou audio)
uploaded_file = st.file_uploader("Choisis un fichier", type=["txt", "mp3", "wav"])

if uploaded_file is not None:
    # Traitement du fichier texte
    if uploaded_file.name.endswith(".txt"):
        # Lire et afficher le contenu du fichier texte
        text = uploaded_file.getvalue().decode("utf-8")
        st.write("Contenu du fichier texte :")
        st.write(text)

        # Ajouter l'analyse ou le résumé du texte ici (exemple simple : afficher les 200 premiers caractères)
        st.write("Analyse du texte :")
        st.write(text[:200] + "...")  # Afficher les 200 premiers caractères

    # Traitement du fichier audio
    elif uploaded_file.name.endswith(".mp3") or uploaded_file.name.endswith(".wav"):
        # Sauvegarder temporairement le fichier audio
        with open("temp_audio.mp3", "wb") as f:
            f.write(uploaded_file.getbuffer())

        # Transcrire l'audio en texte avec Whisper
        st.write("Transcription en cours...")

        # Transcription de l'audio
        result = model.transcribe("temp_audio.mp3")

        # Afficher le texte transcrit
        st.write("Texte transcrit :")
        st.write(result['text'])

    else:
        st.write("Format de fichier non supporté. Veuillez télécharger un fichier texte (.txt) ou audio (.mp3, .wav).")

    # Feedback utilisateur
    feedback = st.text_input("Quel est ton avis sur l'analyse ?")
    if feedback:
        st.write("Merci pour ton retour !")

