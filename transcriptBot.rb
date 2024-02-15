class Transcriptbot < Formula
  desc "Telegram bot for transcript audio messages"
  homepage "https://github.com/kevinm6/audioToText-bot"
  url "file:///path/to/audioToText-bot.tar.gz"
  version "0.1.1"
  license "MIT"
  sha256 :no_check

  depends_on macos: :high_sierra

  def install
    bin.install "transcriptBot"
  end

  service do
    run macos: [opt_bin/"transcriptBot"]
    environment_variables BOT_TOKEN: "token_from_bot_father", VIRTUAL_ENV: "path_to_python_venv_of_bot"
    keep_alive true
    log_path var/"log/transcriptBot/audioToText-bot.stdout.log"
    error_log_path var/"log/transcriptBot/audioToText-bot.stderr.log"
  end
end
