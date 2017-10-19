package mqtt;

import org.eclipse.paho.client.mqttv3.MqttClient;
import org.eclipse.paho.client.mqttv3.MqttConnectOptions;
import org.eclipse.paho.client.mqttv3.MqttException;
import org.eclipse.paho.client.mqttv3.MqttMessage;
import org.eclipse.paho.client.mqttv3.persist.MemoryPersistence;

public class MqttPaho {

	MqttClient sampleClient = null;
	MemoryPersistence persistence = null;
	MqttConnectOptions connOpts;

	String topic = "tag1";
	String content = "Message from MqttPublishSample";
	int qos = 2;

	String broker = "tcp://127.0.0.1:61613";

	String clientId = "JavaSample";
	String userName = "admin";
	String passWord = "password";

	int connectionTimeout = 10;
	int keepAliveInterval = 30;

	public static void main(String[] args) {
		MqttPaho client = new MqttPaho();
		if( client.connect() ) {
			client.publish();
		}
		client.disconnect();		
	}

	boolean connect() {
		try {
			persistence = new MemoryPersistence();
			sampleClient = new MqttClient(broker, clientId, persistence);

			connOpts = new MqttConnectOptions();
			connOpts.setCleanSession(true);
			connOpts.setUserName(userName);
			connOpts.setPassword(passWord.toCharArray());
			connOpts.setConnectionTimeout(connectionTimeout);
			connOpts.setKeepAliveInterval(keepAliveInterval);

			System.out.println("Connecting to broker: " + broker);
			sampleClient.connect(connOpts);
			System.out.println("Connected");

			return true;

		} catch (MqttException me) {
			System.out.println("reason " + me.getReasonCode());
			System.out.println("msg " + me.getMessage());
			System.out.println("loc " + me.getLocalizedMessage());
			System.out.println("cause " + me.getCause());
			System.out.println("excep " + me);
			me.printStackTrace();
		}
		return false;
	}

	boolean disconnect() {
		try {
			sampleClient.disconnect();
			System.out.println("Disconnected");
			return true;

		} catch (MqttException me) {
			System.out.println("reason " + me.getReasonCode());
			System.out.println("msg " + me.getMessage());
			System.out.println("loc " + me.getLocalizedMessage());
			System.out.println("cause " + me.getCause());
			System.out.println("excep " + me);
			me.printStackTrace();
		}
		return false;
	}

	void publish() {
		try {
			System.out.println("Publishing message: " + content);
			
			int count = 1000;
			while( count-->0 ) {
				String value = content + count;
				MqttMessage message = new MqttMessage(value.getBytes());
				message.setQos(qos);
				sampleClient.publish(topic, message);
				System.out.println("Message published");
				try {
					Thread.sleep(100);
				} catch (InterruptedException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
			}

		} catch (MqttException me) {
			System.out.println("reason " + me.getReasonCode());
			System.out.println("msg " + me.getMessage());
			System.out.println("loc " + me.getLocalizedMessage());
			System.out.println("cause " + me.getCause());
			System.out.println("excep " + me);
			me.printStackTrace();
		}
	}
}
