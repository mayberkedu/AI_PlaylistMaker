import streamlit as st
import pandas as pd
from data_collection import extract_playlist_tracks, get_lyrics

# Sayfa yapılandırması
st.set_page_config(
    page_title="AIPlaylistMaker",
    page_icon="🎵",
    layout="wide"
)

st.title("🎵 AIPlaylistMaker")
st.markdown("Spotify çalma listenizi analiz edip AI destekli öneriler sunan akıllı asistanınız.")

# Sekmeleri oluştur
tab1, tab2 = st.tabs(["📊 Playlist Analizi", "🤖 AI Chatbot"])

with tab1:
    st.header("Çalma Listesi Analizi")
    playlist_url = st.text_input("Spotify Çalma Listesi Linkini Girin:", placeholder="https://open.spotify.com/playlist/...")

    if st.button("Listeyi Getir"):
        if playlist_url:
            with st.spinner("Şarkılar Spotify'dan çekiliyor..."):
                tracks, error_msg = extract_playlist_tracks(playlist_url)

            if tracks:
                st.success(f"Başarıyla {len(tracks)} şarkı çekildi!")
                # Veriyi DataFrame'e çevir ve göster
                df = pd.DataFrame(tracks)
                st.dataframe(df, use_container_width=True)

                # Test amaçlı: İlk şarkının sözlerini çekmeyi deneyebiliriz
                first_track = tracks[0]
                with st.expander(f"Örnek Söz Testi: {first_track['track_name']} - {first_track['artist']}"):
                    with st.spinner("Genius'tan sözler aranıyor..."):
                        lyrics = get_lyrics(first_track['track_name'], first_track['artist'])
                        if lyrics:
                            st.text(lyrics)
                        else:
                            st.warning("Şarkı sözü bulunamadı.")
            else:
                if error_msg:
                    st.error(f"Hata oluştu: {error_msg}")
                else:
                    st.error("Çalma listesi boş veya link geçersiz.")
        else:
            st.warning("Lütfen geçerli bir Spotify Çalma Listesi linki girin.")

with tab2:
    st.header("AI Chatbot (Yakında)")
    st.info("Bu özellik henüz geliştirilme aşamasındadır. Yakında çalma listenize dayalı sohbet ve yapay zeka önerileri burada olacak.")
