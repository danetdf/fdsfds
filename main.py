import webbrowser
from kivy.app import App
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

URL = "https://app.diagrams.net/#R7Zttd6I4FMc/DS/rIYEAeenjzsxO53S32+72JZVUmUHjwTjWfvoNIcBFUGurltZ65uQMN48kv/xzkxTD6k4eH8KIGdgc87kwrJ6BsT+btYLQH8X+ZN6aMiFNhtU3zLZMlfyzujpWPkz9CUtzGT3TaCOjhwwPq9BMLJ007KnQU3YntV+gJBM2wyDNf3n1NL7tf//L+db7yoJbZAvUXa85q3/y+Efsz8aXPGCRtASPaRGWTUlaaLBKLYjaZmoZxVlFqDBch0+69ShLtggDNi8lFJxHIpyVjUM+nbKhKNn8OObLcrIHHpVrnfkjVjFcD/2oav03DMQ4tXrYLexfWDgaZzUjh6YxEz9LrN9kPvYDvgSmakdm3RlzLjZGF33eZVEEBkzXY+DB/nnz14zZVLy+uJvg5unH37fuP7w/uLv8OUL3wewCO2mJLKh0eVGrNs3FKhuBJPm1fuSxGPMRn/pRv7B2Yr6YBiypWjamU6T5zvlMGpE0/mRCrDRd/kJwaRqLSaRjt41GBXTGJ0zEK/kcs8gX4e/yy/gauFGe7nllFzVc8VD2Bjb1JLKp23KttHA9i2xstqxydXO+iIdMZ33euL2gXkfWaxY/bJcbIfx4xMQLGmFJZRmAvt0FnEqtmNsbTbH4Mb8hpGv+2V4tV4PVvffl+gI/B8QCs4QZPx5qnkhC3XIcCnY984eJZSnFsEzYXMT8V64gkojOA58KXQCyNYPY/O1HC6DfnYEK+yrsKLW2VOgqCwFa3k/et8iSSnsq/11l6YJkKgrnC0K6OMiQZHlliEHVXZ2YumANsevWk6RVradwpl+HxYI9gg59wSwbA3l1tCgtCynObRm2Lm1RSkxH0mlSxy4BbHlJpOdSgjzTxdbmKfs84Ts0h9azOBzzyf1ifjToKGQnpyCHDg51O4PIBrDgjM3c54Cc9pS9o/5PDWtwHFCQWUOKvUaKt4UUu+Gk2I0ghZRJUVpTyNDa+NuZftXGOoAjUtUUoFY5RLiiVh7QMitrm8p1NNDQK0FzLBuChmnTSCOvWRu947EHEdokPF6FzByJPghTgOku9hBI4ILsA7COoorIrdU7AIKKym2Ay+2pVs99UHXLmtg8VJ1GiGIfiNOgsvPGZTBzoDoV+cxxsEHiKuM2QLXT3AXVow2Hx22uztW6UzZQnTWFg5451WBgEwhPlSVc8flwnesGJCpdY2u0jYBTJQ+0pFPZmGBQSP5G6UQY1PkRm2S+rUs+CvnuK/ccyCTNdiW9hm5+aRsMeq+E1lEGmlQHGq0NNMHbBhq5zR5o2lCF65XdLChRbeDQd8Ds31f2tleRqw7c55p1uxoYRSsupnUcML0aML0ymOnqugFM4jV8i5HtoZpGZhsBWsjWS5Rj735PtB/YiysPNdylQ2iPGwd1gL77jPgVNxMASDYN2sntlHy8j/jw12ZGdfmohln2GIr/krJbRD/dJVEtU1Ugex5EJo936tHUaa9YHMrxYbFunUqybtQ3bupcf/e5JZw+R75SeSOg8AGBsj6B2nW8uX4dkq3wHxMu6yzgQjkwd2WaTgYXrYerV9oON+hKWPa9vwLlzJIL1vl+pWy85qXbDm2IVbvC73u3LNOn7/Ae7oKRfcBpaL/XaYictR+cluiU0/JEmt+cCbntjMHxznBCkrOYkG/vdJEGrItv5Ho5B0SMfCK264bu428U3QMC5XwCtevW7rw2it5ZwLXVQwWs3ZVA/NwoHskvRYhscUypfQDH9IV1O9g+P6eYHlADaIMXGDmepd+29aYu7XGXn+zm6sM7NNnnIAfhLeu19+bRnGTRcU9O1Ps4i0QmtWv+vOJDqzw+5AWm+7mN2PU3UO9QxlWaDR8MZvgW32aWPxuVsdmXo2mEzqC+QFWW/wE="


def open_url(url):
    try:  # Android: системный браузер через Intent
        from jnius import autoclass
        Intent = autoclass("android.content.Intent")
        Uri = autoclass("android.net.Uri")
        activity = autoclass("org.kivy.android.PythonActivity").mActivity
        activity.startActivity(Intent(Intent.ACTION_VIEW, Uri.parse(url)))
    except Exception:  # ПК
        webbrowser.open(url)


class SchemaApp(App):
    def build(self):
        box = BoxLayout(orientation="vertical", padding=30, spacing=20)
        box.add_widget(Label(text="Блок-схема: подозрительное вложение",
                             font_size="20sp"))
        box.add_widget(Button(text="Открыть схему в draw.io",
                              on_release=lambda *_: open_url(URL)))
        return box

    def on_start(self):
        Clock.schedule_once(lambda dt: open_url(URL), 0.5)  # автозапуск


SchemaApp().run()
