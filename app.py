import streamlit as st
import whisper
import os

# Charger le modèle Whisper
st.title("Analyse AI des Appels de Setting")
st.write("Téléverse ton fichier audio ou texte pour commencer.")

try:
    model = whisper.load_model("base")
except Exception as e:
    st.error(f"Erreur lors du chargement du modèle Whisper : {e}")
    st.stop()

# Téléchargement du fichier (texte ou audio)
uploaded_file = st.file_uploader("Choisis un fichier", type=["txt", "mp3", "wav", "m4a"])

if uploaded_file is not None:
    # Identifier le type de fichier
    if uploaded_file.name.endswith(".txt"):
        # Traitement des fichiers texte
        try:
            text = uploaded_file.getvalue().decode("utf-8")
            st.write("Contenu du fichier texte :")
            st.write(text)
            st.write("Analyse du texte :")
            st.write(text[:200] + "...")  # Afficher les 200 premiers caractères
        except Exception as e:
            st.error(f"Erreur lors du traitement du fichier texte : {e}")
    elif uploaded_file.name.endswith((".mp3", ".wav", ".m4a")):
        try:
            # Sauvegarder temporairement le fichier audio
            temp_audio_path = os.path.join(os.getcwd(), "temp_audio.m4a")
            with open(temp_audio_path, "wb") as f:
                f.write(uploaded_file.getbuffer())

            # Transcrire l'audio en texte avec Whisper
            st.write("Transcription en cours...")
            result = model.transcribe(temp_audio_path)

            # Afficher le texte transcrit
            st.write("Texte transcrit :")
            st.write(result['text'])

            # Supprimer le fichier temporaire après traitement
            os.remove(temp_audio_path)
        except Exception as e:
            st.error(f"Erreur lors de la transcription audio : {e}")
    else:
        st.warning("Format de fichier non supporté. Télécharge un fichier texte (.txt) ou audio (.mp3, .wav, .m4a).")

    # Feedback utilisateur
    feedback = st.text_input("Quel est ton avis sur l'analyse ?")
    if feedback:
        st.success("Merci pour ton retour !")
