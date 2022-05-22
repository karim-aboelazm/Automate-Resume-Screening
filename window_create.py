import streamlit as st
import streamlit.components.v1 as components
from pathlib import Path
import base64,random
def img_to_bytes(img_path):
    img_bytes = Path(img_path).read_bytes()
    encoded = base64.b64encode(img_bytes).decode()
    return encoded

def website():
    components.html(
        f"""
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
        <link href="https://fonts.googleapis.com/css?family=Open+Sans:300,300i,400,400i,600,600i,700,700i|Nunito:300,300i,400,400i,600,600i,700,700i|Poppins:300,300i,400,400i,500,500i,600,600i,700,700i" rel="stylesheet">
        <section id="hero" class="hero d-flex align-items-center">

        <div class="container">
        <div class="row mb-5">
            <div class="col-lg-6 d-flex flex-column justify-content-center">
            <h1 data-aos="fade-up">We offer modern solutions for growing your business</h1>
            <h2 data-aos="fade-up" data-aos-delay="400">We are team of talented designers making websites with Bootstrap</h2>
            <div data-aos="fade-up" data-aos-delay="600">
                <div class="text-center text-lg-start" style='margin-top:50px;'>
                <a href="#"  class="btn-get-started scrollto d-inline-flex align-items-center justify-content-center align-self-center">
                    <span>Get Started</span>
                    <i class="bi bi-arrow-right"></i>
                </a>
                </div>
            </div>
            </div>
            <div class="col-lg-6 hero-img" data-aos="zoom-out" data-aos-delay="200">
            <img src='data:image/png;base64,{img_to_bytes("hero-img.png")}' class='img-fluid'>
            </div>
        </div>
        </div>

    </section><!-- End Hero -->
    <main id="main">
        <!-- ======= About Section ======= -->
        <section id="about" class="about">
        <div class="container" data-aos="fade-up">
            <div class="row gx-0">
            <div class="col-lg-6 d-flex flex-column justify-content-center" data-aos="fade-up" data-aos-delay="200">
                <div class="content">
                <h3>Who We Are</h3>
                <h2>Expedita voluptas omnis cupiditate totam eveniet nobis sint iste. Dolores est repellat corrupti reprehenderit.</h2>
                <p>
                    Quisquam vel ut sint cum eos hic dolores aperiam. Sed deserunt et. Inventore et et dolor consequatur itaque ut voluptate sed et. Magnam nam ipsum tenetur suscipit voluptatum nam et est corrupti.
                </p>
                <div class="text-center text-lg-start">
                    <a href="#" class="btn-read-more d-inline-flex align-items-center justify-content-center align-self-center">
                    <span>Read More</span>
                    <i class="bi bi-arrow-right"></i>
                    </a>
                </div>
                </div>
            </div>
            <div class="col-lg-6 d-flex align-items-center" data-aos="zoom-out" data-aos-delay="200">
                <img src='data:image/png;base64,{img_to_bytes("about.jpg")}' class='img-fluid'>
            </div>
            </div>
        </div>
            </section><!-- End About Section -->
            
            <!-- ======= Values Section ======= -->
        <section id="values" class="values mt-5">

        <div class="container" data-aos="fade-up">

            <header class="section-header text-center mb-3">
            <h2>Our Values</h2>
            <p>Odit est perspiciatis laborum et dicta</p>
            </header>

            <div class="row">

            <div class="col-lg-4" data-aos="fade-up" data-aos-delay="200">
                <div class="box">
                <img src='data:image/png;base64,{img_to_bytes("values-1.png")}' class='img-fluid'>
                <h3>Ad cupiditate sed est odio</h3>
                <p>Eum ad dolor et. Autem aut fugiat debitis voluptatem consequuntur sit. Et veritatis id.</p>
                </div>
            </div>

            <div class="col-lg-4 mt-4 mt-lg-0" data-aos="fade-up" data-aos-delay="400">
                <div class="box">
                
                <img src='data:image/png;base64,{img_to_bytes("values-2.png")}' class='img-fluid'>
                <h3>Voluptatem voluptatum alias</h3>
                <p>Repudiandae amet nihil natus in distinctio suscipit id. Doloremque ducimus ea sit non.</p>
                </div>
            </div>

            <div class="col-lg-4 mt-4 mt-lg-0" data-aos="fade-up" data-aos-delay="600">
                <div class="box">
                
                <img src='data:image/png;base64,{img_to_bytes("values-3.png")}' class='img-fluid'>
                <h3>Fugit cupiditate alias nobis.</h3>
                <p>Quam rem vitae est autem molestias explicabo debitis sint. Vero aliquid quidem commodi.</p>
                </div>
            </div>

            </div>

        </div>

        </section><!-- End Values Section -->
        <!-- ======= Features Section ======= -->
        <section id="features" class="features">

        <div class="container" data-aos="fade-up">


            <header class="section-header">
            <h2 class="text-center mt-5">Features</h2>
            <h3>Laboriosam et omnis fuga quis dolor direda fara</h3>
            </header>

            <div class="row">

            <div class="col-lg-6">
                <img src='data:image/png;base64,{img_to_bytes("features.png")}' class='img-fluid'>
            </div>

            <div class="col-lg-6 mt-5 mt-lg-0 d-flex">
                <div class="row align-self-center gy-4">

                <div class="col-md-6" data-aos="zoom-out" data-aos-delay="200">
                    <div class="feature-box d-flex align-items-center">
                    <i class="bi bi-check"></i>
                    <h3>Eos aspernatur rem</h3>
                    </div>
                </div>

                <div class="col-md-6" data-aos="zoom-out" data-aos-delay="300">
                    <div class="feature-box d-flex align-items-center">
                    <i class="bi bi-check"></i>
                    <h3>Facilis neque ipsa</h3>
                    </div>
                </div>

                <div class="col-md-6" data-aos="zoom-out" data-aos-delay="400">
                    <div class="feature-box d-flex align-items-center">
                    <i class="bi bi-check"></i>
                    <h3>Volup amet voluptas</h3>
                    </div>
                </div>

                <div class="col-md-6" data-aos="zoom-out" data-aos-delay="500">
                    <div class="feature-box d-flex align-items-center">
                    <i class="bi bi-check"></i>
                    <h3>Rerum omnis sint</h3>
                    </div>
                </div>

                <div class="col-md-6" data-aos="zoom-out" data-aos-delay="600">
                    <div class="feature-box d-flex align-items-center">
                    <i class="bi bi-check"></i>
                    <h3>Alias possimus</h3>
                    </div>
                </div>

                <div class="col-md-6" data-aos="zoom-out" data-aos-delay="700">
                    <div class="feature-box d-flex align-items-center">
                    <i class="bi bi-check"></i>
                    <h3>Repellendus mollitia</h3>
                    </div>
                </div>

                </div>
            </div>

            </div> <!-- / row -->

            <!-- Feature Tabs -->
            <div class="row feture-tabs" data-aos="fade-up">
            <div class="col-lg-6">
                <h3>Neque officiis dolore maiores et exercitationem quae est seda lidera pat claero</h3>
                <!-- Tab Content -->
                <div class="tab-content">

                <div class="tab-pane fade show active" id="tab1">
                    <p>Consequuntur inventore voluptates consequatur aut vel et. Eos doloribus expedita. Sapiente atque consequatur minima nihil quae aspernatur quo suscipit voluptatem.</p>
                    <div class="d-flex align-items-center mb-2">
                    <i class="bi bi-check2"></i>
                    <h4>Repudiandae rerum velit modi et officia quasi facilis</h4>
                    </div>
                    <p>Laborum omnis voluptates voluptas qui sit aliquam blanditiis. Sapiente minima commodi dolorum non eveniet magni quaerat nemo et.</p>
                    <div class="d-flex align-items-center mb-2">
                    <i class="bi bi-check2"></i>
                    <h4>Incidunt non veritatis illum ea ut nisi</h4>
                    </div>
                    <p>Non quod totam minus repellendus autem sint velit. Rerum debitis facere soluta tenetur. Iure molestiae assumenda sunt qui inventore eligendi voluptates nisi at. Dolorem quo tempora. Quia et perferendis.</p>
                </div><!-- End Tab 1 Content -->

                <div class="tab-pane fade show" id="tab2">
                    <p>Consequuntur inventore voluptates consequatur aut vel et. Eos doloribus expedita. Sapiente atque consequatur minima nihil quae aspernatur quo suscipit voluptatem.</p>
                    <div class="d-flex align-items-center mb-2">
                    <i class="bi bi-check2"></i>
                    <h4>Repudiandae rerum velit modi et officia quasi facilis</h4>
                    </div>
                    <p>Laborum omnis voluptates voluptas qui sit aliquam blanditiis. Sapiente minima commodi dolorum non eveniet magni quaerat nemo et.</p>
                    <div class="d-flex align-items-center mb-2">
                    <i class="bi bi-check2"></i>
                    <h4>Incidunt non veritatis illum ea ut nisi</h4>
                    </div>
                    <p>Non quod totam minus repellendus autem sint velit. Rerum debitis facere soluta tenetur. Iure molestiae assumenda sunt qui inventore eligendi voluptates nisi at. Dolorem quo tempora. Quia et perferendis.</p>
                </div><!-- End Tab 2 Content -->

                <div class="tab-pane fade show" id="tab3">
                    <p>Consequuntur inventore voluptates consequatur aut vel et. Eos doloribus expedita. Sapiente atque consequatur minima nihil quae aspernatur quo suscipit voluptatem.</p>
                    <div class="d-flex align-items-center mb-2">
                    <i class="bi bi-check2"></i>
                    <h4>Repudiandae rerum velit modi et officia quasi facilis</h4>
                    </div>
                    <p>Laborum omnis voluptates voluptas qui sit aliquam blanditiis. Sapiente minima commodi dolorum non eveniet magni quaerat nemo et.</p>
                    <div class="d-flex align-items-center mb-2">
                    <i class="bi bi-check2"></i>
                    <h4>Incidunt non veritatis illum ea ut nisi</h4>
                    </div>
                    <p>Non quod totam minus repellendus autem sint velit. Rerum debitis facere soluta tenetur. Iure molestiae assumenda sunt qui inventore eligendi voluptates nisi at. Dolorem quo tempora. Quia et perferendis.</p>
                </div><!-- End Tab 3 Content -->

                </div>

            </div>

            <div class="col-lg-6">
                <img src='data:image/png;base64,{img_to_bytes("features-2.png")}' class='img-fluid'>
            </div>

            </div><!-- End Feature Tabs -->

            <!-- Feature Icons -->
            <div class="row feature-icons" data-aos="fade-up">
            <h3>Ratione mollitia eos ab laudantium rerum beatae quo</h3>

            <div class="row">

                <div class="col-xl-4 text-center" data-aos="fade-right" data-aos-delay="100">
                <img src='data:image/png;base64,{img_to_bytes("features-3.png")}' class='img-fluid'>
                </div>

                <div class="col-xl-8 d-flex content">
                <div class="row align-self-center gy-4">

                    <div class="col-md-6 icon-box" data-aos="fade-up">
                    <i class="ri-line-chart-line"></i>
                    <div>
                        <h4>Corporis voluptates sit</h4>
                        <p>Consequuntur sunt aut quasi enim aliquam quae harum pariatur laboris nisi ut aliquip</p>
                    </div>
                    </div>

                    <div class="col-md-6 icon-box" data-aos="fade-up" data-aos-delay="100">
                    <i class="ri-stack-line"></i>
                    <div>
                        <h4>Ullamco laboris nisi</h4>
                        <p>Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt</p>
                    </div>
                    </div>

                    <div class="col-md-6 icon-box" data-aos="fade-up" data-aos-delay="200">
                    <i class="ri-brush-4-line"></i>
                    <div>
                        <h4>Labore consequatur</h4>
                        <p>Aut suscipit aut cum nemo deleniti aut omnis. Doloribus ut maiores omnis facere</p>
                    </div>
                    </div>

                    <div class="col-md-6 icon-box" data-aos="fade-up" data-aos-delay="300">
                    <i class="ri-magic-line"></i>
                    <div>
                        <h4>Beatae veritatis</h4>
                        <p>Expedita veritatis consequuntur nihil tempore laudantium vitae denat pacta</p>
                    </div>
                    </div>

                    <div class="col-md-6 icon-box" data-aos="fade-up" data-aos-delay="400">
                    <i class="ri-command-line"></i>
                    <div>
                        <h4>Molestiae dolor</h4>
                        <p>Et fuga et deserunt et enim. Dolorem architecto ratione tensa raptor marte</p>
                    </div>
                    </div>

                    <div class="col-md-6 icon-box" data-aos="fade-up" data-aos-delay="500">
                    <i class="ri-radar-line"></i>
                    <div>
                        <h4>Explicabo consectetur</h4>
                        <p>Est autem dicta beatae suscipit. Sint veritatis et sit quasi ab aut inventore</p>
                    </div>
                    </div>

                </div>
                </div>

            </div>

            </div><!-- End Feature Icons -->

        </div>

        </section><!-- End Features Section -->

        <main>
        <style>
        a {{
            color: #4154f1;
            text-decoration: none;
            }}

        a:hover {{
            color: #717ff5;
            text-decoration: none;
            }}

        h1, h2, h3, h4, h5, h6 {{
            font-family: "Nunito", sans-serif;
            }}
        .hero {{
            width: 100%;
            height: auto;
            background: url('C:/Users/top/Desktop/FlexStart/assets/img/hero-bg.png') top center no-repeat;
            background-size: cover;
            }}
        .hero h1 {{
            margin: 0;
            font-size: 48px;
            font-weight: 700;
            color: #012970;
            }}
            .hero h2 {{
            color: #444444;
            margin: 15px 0 0 0;
            font-size: 26px;
            }}
        .hero .btn-get-started {{
            margin-top: 30px;
            line-height: 0;
            padding: 15px 40px;
            border-radius: 4px;
            transition: 0.5s;
            color: #fff;
            background: #4154f1;
            box-shadow: 0px 5px 30px rgba(65, 84, 241, 0.4);
            }}
        .hero .btn-get-started span {{
            font-family: "Nunito", sans-serif;
            font-weight: 600;
            font-size: 16px;
            letter-spacing: 1px;
            }}
            .hero .btn-get-started i {{
            margin-left: 5px;
            font-size: 18px;
            transition: 0.3s;
            }}
        .hero .btn-get-started:hover i {{
            transform: translateX(5px);
            }}
            .hero .hero-img {{
            text-align: right;
            
            }}
        @media (min-width: 1024px) {{
            .hero {{
                background-attachment: fixed;
            }}
            }}
        .about .content {{
            background-color: #f6f9ff;
            padding: 40px;
            }}
        .about h3 {{
            font-size: 14px;
            font-weight: 700;
            color: #4154f1;
            text-transform: uppercase;
            }}
        .about h2 {{
            font-size: 24px;
            font-weight: 700;
            color: #012970;
            }}
        .about p {{
            margin: 15px 0 30px 0;
            line-height: 24px;
            }}
        .about .btn-read-more {{
            line-height: 0;
            padding: 15px 40px;
            border-radius: 4px;
            transition: 0.5s;
            color: #fff;
            background: #4154f1;
            box-shadow: 0px 5px 25px rgba(65, 84, 241, 0.3);
            }}
        .about .btn-read-more span {{
            font-family: "Nunito", sans-serif;
            font-weight: 600;
            font-size: 16px;
            letter-spacing: 1px;
            }}
        .about .btn-read-more i {{
            margin-left: 5px;
            font-size: 18px;
            transition: 0.3s;
            }}
        .about .btn-read-more:hover i {{
            transform: translateX(5px);
            }}
            .values .box {{
            padding: 30px;
            box-shadow: 0px 0 5px rgba(1, 41, 112, 0.08);
            text-align: center;
            transition: 0.3s;
            height: 100%;
            }}
            .values .box img {{
            padding: 30px 50px;
            transition: 0.5s;
            transform: scale(1.1);
            }}
            .values .section-header p{{
                
                margin: 10px 0 0 0;
                padding: 0;
                font-size: 38px;
                line-height: 42px;
                font-weight: 700;
                color: #012970;

            }}
            .values .section-header h2{{
                font-size: 13px;
                letter-spacing: 1px;
                font-weight: 700;
                margin: 0;
                color: #4154f1;
                text-transform: uppercase;
            }}
            .values .box h3 {{
                font-size: 24px;
                color: #012970;
                font-weight: 700;
                margin-bottom: 18px;
            }}
            .values .box:hover {{
                box-shadow: 0px 0 30px rgba(1, 41, 112, 0.08);
            }}
            .values .box:hover img {{
                transform: scale(1);
            }}
            
            .features .feature-box {{
                padding: 24px 20px;
                box-shadow: 0px 0 30px rgba(1, 41, 112, 0.08);
                transition: 0.3s;
                height: 100%;
                }}
                .features .feature-box h3 {{
                font-size: 18px;
                color: #012970;
                font-weight: 700;
                margin: 0;
                }}
                .features .feature-box i {{
                line-height: 0;
                background: #ecf3ff;
                padding: 4px;
                margin-right: 10px;
                font-size: 24px;
                border-radius: 3px;
                transition: 0.3s;
                }}
                .features .feature-box:hover i {{
                background: #4154f1;
                color: #fff;
                }}
                .features .feture-tabs {{
                margin-top: 120px;
                }}
                .features .feture-tabs h3 {{
                color: #012970;
                font-weight: 700;
                font-size: 32px;
                margin-bottom: 10px;
                }}
                @media (max-width: 768px) {{
                .features .feture-tabs h3 {{
                    font-size: 28px;
                }}
                }}
                .features .feture-tabs .nav-pills {{
                border-bottom: 1px solid #eee;
                }}
                .features .feture-tabs .nav-link {{
                background: none;
                text-transform: uppercase;
                font-size: 15px;
                font-weight: 600;
                color: #012970;
                padding: 12px 0;
                margin-right: 25px;
                margin-bottom: -2px;
                border-radius: 0;
                }}
                .features .feture-tabs .nav-link.active {{
                color: #4154f1;
                border-bottom: 3px solid #4154f1;
                }}
                .features .feture-tabs .tab-content h4 {{
                font-size: 18px;
                margin: 0;
                font-weight: 700;
                color: #012970;
                }}
                .features .feture-tabs .tab-content i {{
                font-size: 24px;
                line-height: 0;
                margin-right: 8px;
                color: #4154f1;
                }}
                .features .feature-icons {{
                margin-top: 120px;
                }}
                .features .feature-icons h3 {{
                color: #012970;
                font-weight: 700;
                font-size: 32px;
                margin-bottom: 20px;
                text-align: center;
                }}
                @media (max-width: 768px) {{
                .features .feature-icons h3 {{
                    font-size: 28px;
                }}
                }}
                .features .feature-icons .content .icon-box {{
                display: flex;
                }}
                .features .feature-icons .content .icon-box h4 {{
                font-size: 20px;
                font-weight: 700;
                margin: 0 0 10px 0;
                color: #012970;
                }}
                .features .feature-icons .content .icon-box i {{
                font-size: 44px;
                line-height: 44px;
                color: #0245bc;
                margin-right: 15px;
                }}
                .features .feature-icons .content .icon-box p {{
                font-size: 15px;
                color: #848484;
                }}
            .features header h2{{
                font-size: 13px;
                letter-spacing: 1px;
                font-weight: 700;
                margin: 0;
                color: #4154f1;
                text-transform: uppercase;
            }}
            .features header h3{{
                margin: 10px 0 10px 0;
                padding: 0;
                font-size: 38px;
                line-height: 42px;
                font-weight: 700;
                color: #012970;
            }}

            </style>
        """,
        height=2500,
        width=1000,
)