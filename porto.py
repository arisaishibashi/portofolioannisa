import streamlit as st
from urllib.parse import urlencode

# ---------- Page Config ----------
st.set_page_config(
    page_title="Portofolio Saya",
    page_icon="🌸",
    layout="centered",
    initial_sidebar_state="expanded",
)

# ---------- Theme Colors ----------
PRIMARY_COLOR = "#FF6F61"   # coral
SECONDARY_COLOR = "#4E342E" # brown
BG_COLOR = "#FFF8E7"        # very light yellow
TEXT_COLOR = "#4E342E"      # <-- tambahkan '#'


# ---------- Global CSS ----------
st.markdown(
    f"""
    <style>
    .main {{
        background-color: {BG_COLOR};
        color: {TEXT_COLOR};
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }}
    .title {{ color: {PRIMARY_COLOR}; font-weight: 700; }}
    .subtitle {{ color: {SECONDARY_COLOR}; font-weight: 600; }}

    /* PROJECT BOX */
    .project-box {{
        border-radius: 10px;
        padding: 15px 20px;
        margin-bottom: 20px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        cursor: pointer;
        transition: all 0.3s ease;
        background-color: #FFB6A3; /* default coral soft */
    }}
    .project-box:hover {{
        background-color: #FF9980; /* coral lebih pekat */
        box-shadow: 0 8px 12px rgba(0,0,0,0.2);
    }}

    a.project-link {{ text-decoration: none; color: inherit; display: block; }}

    /* Sidebar */
    section[data-testid="stSidebar"] {{ background-color: #FFF8E7; }}
    div[role="radiogroup"] label {{
        background-color: #FFEFD5;
        border-radius: 10px;
        padding: 8px 12px;
        margin: 5px 0;
        cursor: pointer;
        transition: all 0.3s ease;
    }}
    div[role="radiogroup"] label:hover {{ background-color: #FFD166; }}
    div[role="radiogroup"] label[data-checked="true"] {{
        background-color: #C6F6D5;
        font-weight: 600;
        box-shadow: 0 4px 6px rgba(0,0,0,0.15);
    }}

    /* Nav link */
    .nav-link {{
        font-weight: 600; font-size: 18px;
        color: {PRIMARY_COLOR};
        text-decoration: none; margin-right: 20px;
    }}
    .nav-link:hover {{ color: {SECONDARY_COLOR}; cursor: pointer; }}

    /* Header atas Streamlit */
    header[data-testid="stHeader"] {{
        background-color: #FFF8E7;
    }}
    header[data-testid="stHeader"] * {{
        color: white !important;
    }}
    </style>
    """,
    unsafe_allow_html=True,
)


# ---------- Data ----------
projects = [
    {
        "id": "web_deteksi_ikan_cnn",
        "title": "Web Deteksi Ikan Air Tawar Menggunakan CNN",
        "summary": "Website yang menggunakan CNN untuk mendeteksi jenis ikan air tawar dari gambar.",
    },
    {   
        "id": "warung_seblakin",
        "title": "Warung Seblakin",
        "summary": "Website untuk memesan makanan secara online dengan fitur utama.",
    },
    {
        "id": "aplikasi_hewan",
        "title": "Aplikasi Pengenalan Hewan Berdasarkan Makanannya",
        "summary": "Aplikasi berbasis android untuk belajar mengenal hewan berdasarkan makanannya.",
    },
]

# ---------- Query Params Helpers ----------
def get_query_params():
    return st.experimental_get_query_params()

def set_query_params(params: dict):
    st.experimental_set_query_params(**params)

# ---------- UI Helpers ----------
def render_slider(images: list, state_key: str):
    """Render slider gambar sederhana dengan prev/next dan indikator titik."""
    if state_key not in st.session_state:
        st.session_state[state_key] = 0

    st.markdown("#### 🎨 Pratinjau UI")
    c1, c2, c3 = st.columns([1, 6, 1])

    with c1:
        if st.button("◀", key=f"{state_key}_prev"):
            st.session_state[state_key] = (st.session_state[state_key] - 1) % len(images)

    with c2:
        current_img, current_cap = images[st.session_state[state_key]]
        st.image(current_img, caption=current_cap, use_column_width=True)

    with c3:
        if st.button("▶", key=f"{state_key}_next"):
            st.session_state[state_key] = (st.session_state[state_key] + 1) % len(images)

    dots = " ".join("●" if i == st.session_state[state_key] else "○" for i in range(len(images)))
    st.markdown(f"<div style='text-align:center;font-size:20px'>{dots}</div>", unsafe_allow_html=True)

# ---------- Pages ----------
def main_page():
    st.markdown('<h1 class="title">Halo, Selamat datang di portofolio Annisa 🌸 </h1>', unsafe_allow_html=True)
    st.markdown(
        """
        <p class="subtitle">
        Salam kenal semuanya! Aku Annisa Solehah 🌸, seseorang yang tertarik dengan dunia teknologi, khususnya pengembangan aplikasi, desain antarmuka, dan pengolahan data 💻✨.
        Aku terus mengembangkan kemampuan melalui berbagai proyek, pelatihan, dan eksplorasi mandiri. 
        Portofolio ini aku susun sebagai rangkuman perjalanan belajar dan karya-karya yang telah aku buat 🌿.
        </p>
        """,
        unsafe_allow_html=True,
    )
    st.write("---")
    st.markdown('<h2 class="title">Project-Project Saya</h2>', unsafe_allow_html=True)

    for project in projects:
        url = f"?{urlencode({'project': project['id']})}"
        st.markdown(
            f"""
            <a href="{url}" class="project-link" target="_self">
                <div class="project-box">
                    <h3>{project['title']}</h3>
                    <p>{project['summary']}</p>
                </div>
            </a>
            """,
            unsafe_allow_html=True,
        )

def project_detail_page(project_id: str):
    project = next((p for p in projects if p["id"] == project_id), None)
    if project is None:
        st.error("Project tidak ditemukan.")
        return

    st.markdown(f'<h1 class="title">{project["title"]}</h1>', unsafe_allow_html=True)
    st.write("---")
    
    # ---- Web Deteksi Ikan CNN ----
    if project_id == "web_deteksi_ikan_cnn":
        images = [
            ("assets/webikan/halaman_utama.png", "Tampilan Halaman Utama"),
            ("assets/webikan/infoweb.png", "Tampilan Halaman Informasi Web"),
            ("assets/webikan/deteksi.png", "Tampilan Halaman Fish Recognition"),
            ("assets/webikan/riwayatdeteksi.png", "Tampilan Halaman Riwayat Deteksi"),
        ]
        render_slider(images, state_key="fish_idx")

        st.write("---")
        st.subheader("ℹ️ Tentang Proyek")
        st.markdown("Website deteksi ikan air tawar berbasis CNN dengan fitur unggah gambar, klasifikasi, dan riwayat deteksi.")

        st.subheader("⚙️ Teknologi yang Digunakan")
        st.markdown(
            """
            - Python (Streamlit) 
            - Convolutional Neural Network
            - Transfer Learning MobileNetV2 
            - Figma (UI/UX Design)
            """
        )
        
        st.subheader("🌐 Tautan Proyek")
        st.markdown(
            """
            🔗 Kunjungi Website Deteksi Ikan (https://deteksi-air-tawar.streamlit.app/)
            """,
            unsafe_allow_html=True,
        )

        if st.button("Kembali ke Halaman Utama", key="back_fish"):
            set_query_params({})
            st.experimental_rerun()
            
    # ---- Warung Seblakin ----
    elif project_id == "warung_seblakin":
        images = [
            ("assets/warung_seblakin/halaman_utama.png", "Tampilan Halaman Utama"),
            ("assets/warung_seblakin/menu.png", "Tampilan Semua Menu"),
            ("assets/warung_seblakin/seblak.png", "Tampilan Menu Seblak"),
            ("assets/warung_seblakin/gorengan.png", "Tampilan Menu Gorengan"),
            ("assets/warung_seblakin/detail.png", "Tampilan Detail Menu"),
            ("assets/warung_seblakin/keranjang.png", "Tampilan Keranjang Belanja"),
            ("assets/warung_seblakin/pengiriman.png", "Tampilan Metode Pengiriman"),
            ("assets/warung_seblakin/nobayar.png", "Tampilan Halaman Pembayaran"),
            ("assets/warung_seblakin/checkout.png", "Tampilan Checkout"),
            ("assets/warung_seblakin/login.png", "Tampilan Halaman Login"),
        ]
        render_slider(images, state_key="ws_idx")

        st.write("---")
        st.subheader("ℹ️ Tentang Proyek")
        st.markdown(
            """
            Website ini merupakan platform pemesanan makanan online. Proyek ini dikerjakan berdasarkan kebutuhan klien yang memiliki usaha warung seblak, sehingga seluruh fitur yang dirancang menyesuaikan dengan alur bisnis dan permintaan klien.
            Website ini memfasilitasi pelanggan untuk melihat menu, melakukan pemesanan, serta mendapatkan informasi terkait produk secara lebih mudah. Dari sisi klien, website ini membantu mengelola data pesanan dengan lebih teratur dan efisien.
            Proses pengembangan dilakukan mulai dari tahap analisis kebutuhan, perancangan, implementasi, hingga pengujian. 
            Hasil akhir website ini tidak hanya menjadi solusi digital bagi klien, tetapi juga menjadi pengalaman berharga bagi saya dalam mengaplikasikan teori pengembangan perangkat lunak ke dalam praktik nyata.
            """
        )

        st.subheader("⚙️ Teknologi yang Digunakan")
        st.markdown(
            """
            - PHP  
            - phpMyAdmin  
            - HTML, CSS  
            - Figma (UI/UX Design)
            """
        )

        if st.button("Kembali ke Halaman Utama", key="back_ws"):
            set_query_params({})
            st.experimental_rerun()


    # ---- Aplikasi hewan (placeholder singkat) ----
    elif project_id == "aplikasi_hewan":
        images = [
            ("assets/hewan/home.jpeg", "Tampilan Halaman Utama"),
            ("assets/hewan/pengaturan.jpeg", "Tampilan Halaman Pengaturan"),
            ("assets/hewan/infoapp.jpeg", "Tampilan Halaman Informasi Aplikasi"), 
            ("assets/hewan/carabermain.jpeg", "Tampilan Halaman Cara Bermain"),
            ("assets/hewan/Menu.jpeg", "Tampilan Halaman Menu"),
            ("assets/hewan/materiherbi.jpeg", "Tampilan Halaman Materi Herbivora"),
            ("assets/hewan/hewanherbi.jpeg", "Tampilan Halaman Hewan Herbivora"),
            ("assets/hewan/materikarni.jpeg", "Tampilan Halaman Materi Karnivora"),
            ("assets/hewan/hewankani.jpeg", "Tampilan Halaman Hewan Karnivora"),
            ("assets/hewan/materiomni.jpeg", "Tampilan Halaman Materi Omnivora"),
            ("assets/hewan/hewanomni.jpeg", "Tampilan Halaman Hewan Omnivora"),
            ("assets/hewan/menugame.jpeg", "Tampilan Halaman Menu Permainan"),
            ("assets/hewan/benar.jpeg", "Tampilan Halaman Pada Kuis Ketika Menjawab Benar"),
            ("assets/hewan/salah.jpeg", "Tampilan Halaman Pada Kuis Ketika Menjawab Salah"),
            ("assets/hewan/game.jpeg", "Tampilan Halaman Permainan"),
            ("assets/hewan/gamehebi.jpeg", "Tampilan Halaman Permainan Tangkap Hewan"),
            ("assets/hewan/arkambing.jpeg", "Tampilan Halaman AR Kambing"),
            ("assets/hewan/arsinga.jpeg", "Tampilan Halaman AR Singa"),
        ]
        render_slider(images, state_key="hewan")

        st.write("---")
        st.subheader("ℹ️ Tentang Proyek")
        st.markdown("""Aplikasi ini merupakan sebuah media edukasi interaktif yang dirancang untuk memperkenalkan hewan berdasarkan jenis makanannya, yaitu herbivora, karnivora, dan omnivora. 
                    Di dalamnya terdapat materi pembelajaran yang disajikan secara sederhana dan menarik, fitur Augmented Reality (AR) yang memungkinkan pengguna memindai gambar untuk menampilkan hewan dalam bentuk 3D, 
                    serta kuis interaktif untuk menguji pemahaman pengguna. 
                    Selain itu, aplikasi ini juga dilengkapi dengan mini game tangkap hewan sesuai makanannya sehingga proses belajar menjadi lebih menyenangkan dan interaktif.""")

        st.subheader("⚙️ Teknologi yang Digunakan")
        st.markdown(
            """
            - C# 
            - Unity
            - Augmented Reality (AR)
            - Figma (UI/UX Design)
            """
        )
        
        st.subheader("🌐 Tautan Proyek")
        st.markdown(
            """
            🔗 Unduh aplikasi (Drive) (https://drive.google.com/file/d/11uc9LSZngrUM0da5BCk2rb62yGsMrZWu/view?usp=drive_link)
            """,
            unsafe_allow_html=True,
        )

        if st.button("Kembali ke Halaman Utama", key="back_hewan"):
            set_query_params({})
            st.experimental_rerun()
            
def data_diri_page():
    st.markdown('<h1 class="title">Data Diri</h1>', unsafe_allow_html=True)
    st.write("---")
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image(
            "assets/aku.jpeg",
            width=200,
        )
    with col2:
        st.markdown(
            """
            <div style="background-color:#FFF8E7; padding:20px; border-radius:15px; 
                        box-shadow:0 4px 6px rgba(0,0,0,0.1);">
                <p><strong>Nama:</strong> Annisa Solehah</p>
                <p><strong>Pendidikan:</strong> S1 Informatika</p>
                <p><strong>Keahlian:</strong></p>
                <ul>
                    <li>Python, java, JavaScript, HTML/CSS</li>
                    <li>Machine Learning & Deep Learning</li>
                    <li>Web Development</li>
                    <li>UI/UX</li>
                    <li>MySQL, PostgreSQL</li> 
                    <li>Microsoft Office</li>
                    
                </ul>
            </div>
            """,
            unsafe_allow_html=True,
        )

def kontak_page():
    st.markdown('<h1 class="title">Informasi Kontak</h1>', unsafe_allow_html=True)
    st.write("---")
    st.markdown(
        """
        <div style="background-color:#FFF8E7; padding:20px; border-radius:15px; 
                    box-shadow:0 4px 6px rgba(0,0,0,0.1); font-size:16px;">
            <p>📧 <strong>Email:</strong> <a href="mailto:annisaslhh43@gmail.com">annisaslhh43@gmail.com</a></p>
            <p>📱 <strong>Telepon:</strong> <a href="tel:+62858881625787">+62 858 881 625 787</a></p>
            <p>💼 <strong>LinkedIn:</strong> <a href="https://www.linkedin.com/in/annisa-solehah/" target="_blank">linkedin.com/in/annisa-solehah</a></p>
            <p>💻 <strong>GitHub:</strong> <a href="https://github.com/arisaishibashi" target="_blank">github.com/arisaishibashi</a></p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown(
        """
        <div style="margin-top: 20px;">
            <a href="mailto:annisaslhh43@gmail.com" style="background-color: #FF6F61; color: white; padding: 10px 20px; border-radius: 5px; text-decoration: none;">Kirim Email</a>
        </div>
        """,
        unsafe_allow_html=True,
    )

# ---------- Sidebar & Router ----------
st.sidebar.title("Navigasi")
page = st.sidebar.radio("Pilih Halaman:", ["Halaman Utama", "Data Diri", "Informasi Kontak"])

query_params = get_query_params()
project_id = query_params.get("project", [None])[0]

if page == "Halaman Utama":
    if project_id:
        project_detail_page(project_id)
    else:
        main_page()
elif page == "Data Diri":
    data_diri_page()
elif page == "Informasi Kontak":
    kontak_page()





