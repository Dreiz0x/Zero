package dreiz0x.vespa

import android.content.Intent
import android.os.Bundle
import android.widget.ImageButton
import androidx.appcompat.app.AppCompatActivity

class WelcomeActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_welcome)

        val btnComenzar = findViewById<ImageButton>(R.id.btnComenzar)

        btnComenzar.animate()
            .alpha(1f)
            .setDuration(1500)
            .setStartDelay(500)
            .start()

        btnComenzar.setOnClickListener {
            startActivity(Intent(this, MainActivity::class.java))
            finish()
        }
    }
}
