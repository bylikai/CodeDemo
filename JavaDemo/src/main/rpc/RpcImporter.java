package rpc;

import java.io.ObjectInputStream;
import java.io.ObjectOutputStream;
import java.lang.reflect.InvocationHandler;
import java.lang.reflect.Method;
import java.lang.reflect.Proxy;
import java.net.InetSocketAddress;
import java.net.Socket;

/**
 * 本地服务代理 <br>
 * 		1、将本地接口调用转换成JDK的动态代理，在动态代理中实现接口的远程调用 <br>
 * 		2、创建Socket客户端，根据指定地址连接远程服务提供者 <br>
 * 		3、将远程服务调用所有的接口类，方法，参数列表，等编码后发送给服务提供者<br>
 * 		4、同步阻塞等待服务返回应答，获取应答后返回<br>
 * @author kaiLee
 *
 * @param <S>
 */
public class RpcImporter<S> {
	
	@SuppressWarnings("unchecked")
	public S importer(final Class<?> serviceClass, final InetSocketAddress addr ) {
		
		return (S) Proxy.newProxyInstance(serviceClass.getClassLoader(), new Class<?>[]{ serviceClass.getInterfaces()[0] } ,
				new InvocationHandler() {
					
					@Override
					public Object invoke(Object proxy, Method method, Object[] args) throws Throwable {
						// TODO Auto-generated method stub
						
						Socket socket = null;
						
						ObjectInputStream	input = null;
						ObjectOutputStream output = null;
						
						try {
							socket = new Socket();
							socket.connect(addr);
							
							output= new ObjectOutputStream( socket.getOutputStream() );
							
							output.writeUTF( serviceClass.getName() );
							output.writeUTF( method.getName() );
							output.writeObject(method.getParameterTypes());
							output.writeObject(args);
							
							input = new ObjectInputStream( socket.getInputStream() );
							
							return input.readObject();
						}
						finally {
							if( null != socket )  socket.close();
							if( null != input )   input.close();
							if( null != output )  output.close();
						}
					}
				} );
	} 
}
