man kann coder in encoder und decoder einteilen:
kurz gesagt,
Der Decoder ließt den Input 
Und der Encoder schreibt den Output

Auf dem Biebertal Server werden wir später für den Decoder den Standard Decoder nutzen,
jedoch für den Encoder den h264_nvenc, dieser läuft über die GPU und nicht über die CPU
und ist somit schneller da die Hardware dafür angepasst ist.

Es gibt auch Coder für die GPU (h264_cuvid und viele andere) diese machen aber nur Sinn wenn man als Input ein
Video hat, da wir in unserem Fall aber images haben,
muss dieses Coding auf der CPU stattfinden.

Es gibt viele weitere Einstellungen wie:
-hwaccel cuvid
sorgt dafür, dads die decodierten frames in der GPU bleiben, dadurch übernimmt die GPU den gesamten
Rechenaufwand was sich aber bei uns nicht einsetzten lässt
-vsync 0
verhindert das Duplizieren oder Löschen von Frames
-c:a copy
sorgt dafür das das audio nicht neu gerendert wird

Ein Bsp für ein kompletes GPU rendern wäre folgendes:
ffmpeg -vsync 0 -hwaccel cuvid -c:v h264_cuvid -i input.mp4 -c:a copy -c:v h264_nvenc  output.mp4



