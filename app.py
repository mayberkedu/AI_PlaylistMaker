import streamlit as st
import pandas as pd
from data_collection import extract_playlist_tracks, get_lyrics
from ai_engine import analyze_playlist_with_gemini, analyze_lyrics_with_gemini, get_recommendations_with_gemini

# Sayfa yapılandırması
st.set_page_config(
    page_title="AIPlaylistMaker",
    page_icon="🎵",
    layout="wide"
)

# Session state (durum) yönetimi
if "tracks" not in st.session_state:
    st.session_state.tracks = None
if "error_msg" not in st.session_state:
    st.session_state.error_msg = None
if "profile" not in st.session_state:
    st.session_state.profile = None
if "recs" not in st.session_state:
    st.session_state.recs = None
if "lyrics" not in st.session_state:
    st.session_state.lyrics = None
if "lyric_analysis" not in st.session_state:
    st.session_state.lyric_analysis = None

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
                st.session_state.tracks, st.session_state.error_msg = extract_playlist_tracks(playlist_url)
                # Eski yapay zeka verilerini sıfırla
                st.session_state.profile = None
                st.session_state.recs = None
                st.session_state.lyrics = None
                st.session_state.lyric_analysis = None
        else:
            st.warning("Lütfen geçerli bir Spotify Çalma Listesi linki girin.")

    if st.session_state.tracks:
        tracks = st.session_state.tracks
        st.success(f"Başarıyla {len(tracks)} şarkı çekildi!")
        # Veriyi DataFrame'e çevir ve göster
        df = pd.DataFrame(tracks)
        st.dataframe(df, use_container_width=True)

        st.divider()
        st.subheader("🤖 Gemini AI ile Çalma Listesi Analizi")

        if st.button("Listeyi Yapay Zeka ile Analiz Et", type="primary"):
            with st.spinner("Gemini API, çalma listenizin müzikal materyalini analiz ediyor..."):
                st.session_state.profile = analyze_playlist_with_gemini(tracks)
                if "error" not in st.session_state.profile:
                    st.session_state.recs = get_recommendations_with_gemini(st.session_state.profile, count=4)

        if st.session_state.profile:
            profile = st.session_state.profile
            if "error" in profile:
                st.error(f"AI Analiz Hatası: {profile['error']}")
            else:
                # Profil Sonuçlarını Göster
                st.success("Analiz Tamamlandı!")

                col1, col2, col3 = st.columns(3)
                col1.metric("Ortalama BPM", profile.get('average_bpm', '-'))
                col2.metric("Ruh Hali", profile.get('mood', '-'))
                col3.metric("Baskın Türler", ", ".join(profile.get('dominant_genres', [])))

                st.info(f"**Konsept:** {profile.get('playlist_concept', '')}")
                st.write(f"**Müzikal Profil:** {profile.get('musical_profile', '')}")

                recs = st.session_state.recs
                if recs:
                    st.subheader("✨ Sizin İçin Şarkı Önerileri")
                    for rec in recs:
                        with st.expander(f"🎵 {rec.get('track_name')} - {rec.get('artist')}"):
                            st.write(f"**Neden önerildi?** {rec.get('reason')}")
                            if rec.get("spotify_url"):
                                st.markdown(f"[🎧 Spotify'da Dinle]({rec.get('spotify_url')})")

        st.divider()
        # Test amaçlı: İlk şarkının sözlerini çekmeyi deneyebiliriz
        first_track = tracks[0]
        st.subheader(f"Örnek Söz & Tema Analizi: {first_track['track_name']} - {first_track['artist']}")

        if st.button("Sözleri Çek ve Analiz Et"):
            with st.spinner("Genius'tan sözler aranıyor ve Gemini ile analiz ediliyor..."):
                lyrics = get_lyrics(first_track['track_name'], first_track['artist'])
                if lyrics:
                    st.session_state.lyrics = lyrics
                    st.session_state.lyric_analysis = analyze_lyrics_with_gemini(lyrics)
                else:
                    st.warning("Şarkı sözü bulunamadı.")
                    st.session_state.lyrics = None
                    st.session_state.lyric_analysis = None

        if st.session_state.lyrics:
            st.text_area("Şarkı Sözleri", st.session_state.lyrics, height=150)

        if st.session_state.lyric_analysis:
            lyric_analysis = st.session_state.lyric_analysis
            st.markdown(f"**Tema:** {lyric_analysis.get('theme')}")
            st.markdown(f"**Duygu:** {lyric_analysis.get('emotion')}")
            st.markdown(f"**Özet:** {lyric_analysis.get('summary')}")

    elif st.session_state.error_msg:
        st.error(f"Hata oluştu: {st.session_state.error_msg}")

with tab2:
    st.header("AI Chatbot (Yakında)")
    st.info("Bu özellik henüz geliştirilme aşamasındadır. Yakında çalma listenize dayalı sohbet ve yapay zeka önerileri burada olacak.")
