import streamlit as st
from urllib.parse import urlencode

# Set page config
st.set_page_config(
    page_title="Portofolio Saya",
    page_icon="🌸",
    layout="centered",
    initial_sidebar_state="expanded",
)

# Warna cheerful
PRIMARY_COLOR = "#FF6F61"  # coral
SECONDARY_COLOR = "#4E342E"  # yellow
BG_COLOR = "#FFF8E7"  # very light yellow
TEXT_COLOR = "4E342E"

# CSS custom untuk styling
st.markdown(
    f"""
    <style>
    .main {{
        background-color: {BG_COLOR};
        color: {TEXT_COLOR};
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }}
    .title {{
        color: {PRIMARY_COLOR};
        font-weight: 700;
    }}
    .subtitle {{
        color: {SECONDARY_COLOR};
        font-weight: 600;
    }}

    /* PROJECT BOX */
    .project-box {{
        border-radius: 10px;
        padding: 15px 20px;
        margin-bottom: 20px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        cursor: pointer;
        transition: all 0.3s ease;
    }}
    /* Default warna (coral soft) */
    .project-box {{
        background-color: #FFB6A3;
    }}
    .project-box:hover {{
        background-color: #FF9980; /* coral lebih pekat */
        box-shadow: 0 8px 12px rgba(0,0,0,0.2);
    }}

    a.project-link {{
        text-decoration: none;
        color: inherit;
        display: block;
    }}

    /* NAVIGASI SIDEBAR */
    section[data-testid="stSidebar"] {{
        background-color: #FFF8E7; /* light cream */
    }}
    section[data-testid="stSidebar"] .css-1d391kg {{
        color: {PRIMARY_COLOR}; /* coral */
        font-weight: 700;
    }}
    div[role="radiogroup"] label {{
        background-color: #FFEFD5; /* soft peach */
        border-radius: 10px;
        padding: 8px 12px;
        margin: 5px 0;
        cursor: pointer;
        transition: all 0.3s ease;
    }}
    div[role="radiogroup"] label:hover {{
        background-color: #FFD166; /* cheerful yellow */
    }}
    div[role="radiogroup"] label[data-checked="true"] {{
        background-color: #C6F6D5; /* soft mint */
        font-weight: 600;
        box-shadow: 0 4px 6px rgba(0,0,0,0.15);
    }}

    /* NAV LINK BIASA */
    .nav-link {{
        font-weight: 600;
        font-size: 18px;
        color: {PRIMARY_COLOR};
        text-decoration: none;
        margin-right: 20px;
    }}
    .nav-link:hover {{
        color: {SECONDARY_COLOR};
        cursor: pointer;
    }}
    </style>
    """,
    unsafe_allow_html=True,
)


# Data project dalam list dictionary
projects = [
    {
        "id": "web_pemesanan_makanan",
        "title": "Web Pemesanan Makanan",
        "summary": "Website untuk memesan makanan secara online dengan fitur utama.",
        "details": """
- Menu makanan lengkap  
- Keranjang belanja  
- Pembayaran online  
- Tracking pesanan  
- Responsive dan user-friendly  
""",
    },
    {
        "id": "web_deteksi_ikan_cnn",
        "title": "Web Deteksi Ikan Air Tawar Menggunakan CNN",
        "summary": "Website yang menggunakan CNN untuk mendeteksi jenis ikan air tawar dari gambar.",
        "details": """
- Upload gambar ikan  
- Prediksi jenis ikan secara real-time  
- Informasi detail tentang ikan  
- Model CNN yang dioptimasi untuk akurasi tinggi  
""",
    },
    {
        "id": "aplikasi_manajemen_tugas",
        "title": "Aplikasi Manajemen Tugas Harian",
        "summary": "Aplikasi web untuk membantu mengelola tugas harian dengan fitur lengkap.",
        "details": """
- Tambah, edit, hapus tugas  
- Tandai tugas selesai  
- Reminder dan notifikasi  
- Tampilan sederhana dan mudah digunakan  
""",
    },
]

def get_query_params():
    query_params = st.experimental_get_query_params()
    return query_params

def set_query_params(params: dict):
    st.experimental_set_query_params(**params)

def main_page():
    st.markdown('<h1 class="title">Halo, Selamat datang di portofolio saya! </h1>', unsafe_allow_html=True)
    st.markdown(
        """
        <p class="subtitle">
        Perkenalkan, saya Annisa Solehah. 
        Saya memiliki ketertarikan pada pengembangan teknologi berbasis web dan kecerdasan buatan.
        Bidang eksplorasi saya meliputi pembuatan deteksi berbasis CNN, 
        desain tampilan web dan aplikasi, pembuatan model deteksi, 
        pengembangan aplikasi Android sederhana, serta sedang memulai perjalanan di bidang data analysis.
        Semoga portofolio ini bisa menjadi jendela kecil untuk mengenal saya lebih dekat.
        </p>
        """,
        unsafe_allow_html=True,
    )

    st.write("---")

    st.markdown('<h2 class="title">Project-Project Saya</h2>', unsafe_allow_html=True)

    # Tampilkan project dalam kotak yang bisa diklik (link)
    for project in projects:
        # Buat URL dengan query param ?project=project_id
        query = urlencode({"project": project["id"]})
        url = f"?{query}"

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

def project_detail_page(project_id):
    # Cari project berdasarkan id
    project = next((p for p in projects if p["id"] == project_id), None)
    if project is None:
        st.error("Project tidak ditemukan.")
        return

    st.markdown(f'<h1 class="title">{project["title"]}</h1>', unsafe_allow_html=True)
    st.write("---")
    st.markdown(f'<p class="subtitle">{project["summary"]}</p>', unsafe_allow_html=True)
    st.markdown(project["details"])

    # Tombol kembali ke halaman utama
    if st.button("← Kembali ke Halaman Utama"):
        set_query_params({})  # Hapus query param untuk kembali ke main page
        st.experimental_rerun()

def data_diri_page():
    st.markdown('<h1 class="title">Data Diri</h1>', unsafe_allow_html=True)
    st.write("---")

    # Gunakan kolom untuk gambar dan info
    col1, col2 = st.columns([1, 2])

    with col1:
        st.image(
            "https://images.unsplash.com/photo-1508214751196-bcfd4ca60f91?auto=format&fit=crop&w=400&q=80",
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
                    <li>Python, JavaScript, HTML/CSS</li>
                    <li>Machine Learning & Deep Learning</li>
                    <li>Web Development (Streamlit, React)</li>
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
            <p>📱 <strong>Telepon:</strong> <a href="tel:+6281234567890">+62 858 881 625 787</a></p>
            <p>💼 <strong>LinkedIn:</strong> <a href="https://www.linkedin.com/in/annisa-solehah/" target="_blank">linkedin.com/in/annisa-solehah</a></p>
            <p>💻 <strong>GitHub:</strong> <a href="https://github.com/arisaishibashi" target="_blank">github.com/arisaishibashi</a></p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown(
        """
        <div style="margin-top: 20px;">
            <a href="mailto:nama.email@example.com" style="background-color: #FF6F61; color: white; padding: 10px 20px; border-radius: 5px; text-decoration: none;">Kirim Email</a>
        </div>
        """,
        unsafe_allow_html=True,
    )

# Sidebar navigasi
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
