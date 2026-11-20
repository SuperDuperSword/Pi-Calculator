import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class AngleMaker {
	
	public ArrayList<Vector2> points = new ArrayList<>(List.of(new Vector2(0, 1), new Vector2(1, 0)));
	public int subdivisions = 16;
	public double curveLength;
	
	
	public AngleMaker(int subdivisions) {
		this.subdivisions = subdivisions;
	}
	
	public AngleMaker() {}
	
	public void subdivide() {
		ArrayList<Vector2> newPoints = new ArrayList<>();
		
		for (int i=0; i<points.size() - 1; i++) {
			Vector2 l = points.get(i);
			Vector2 r = points.get(i+1);
			
			Vector2 avg = l.averageWith(r);
			newPoints.add(avg.normalized());
		}
		
		int insertionIndex = 1;
		for (Vector2 point : newPoints) {
			points.add(insertionIndex, point);
			insertionIndex += 2;
		}
	}
	
	public void recalculate() {
		points = new ArrayList<>(List.of(new Vector2(0, 1), new Vector2(1, 0)));
		
		for (int i=0; i<subdivisions; i++) {
			subdivide();
		}
		
		updateCurveLength();
	}
	
	public void updateCurveLength() {
		curveLength = 0;
		for (int i=0; i< points.size() - 1; i++) {
			Vector2 l = points.get(i);
			Vector2 r = points.get(i+1);
			
			double difference = l.distanceTo(r);
			curveLength += difference;
		}
	}
	
	public long recalculateAndProfile(){
		long beginTime = System.currentTimeMillis();
		recalculate();
		return System.currentTimeMillis() - beginTime;
	}
	
	public static void main(String[] args) {
		AngleMaker angleMaker = new AngleMaker();
		
		Scanner scan = new Scanner(System.in);
		
		System.out.println("This program will calculate pi to any arbitrary precision.");
		System.out.println("math.pi is always greater than the calculation due to how it's calculated.");
		System.out.println("If you want, you can change the precision to whatever you want.");
		System.out.println("The default is " + angleMaker.subdivisions + ", and the computation time grows exponentially with that number.");
		System.out.print("If you don't enter anything, it will use that default. Please enter your desired precision: ");

		String input = scan.nextLine();
		try{
			angleMaker.subdivisions = Integer.parseInt(input);
		} catch(NumberFormatException ignored){
		
		}
		
		long elapsedTime = angleMaker.recalculateAndProfile();
		System.out.println();
		System.out.println("Performing " + angleMaker.subdivisions + " subdivisions took " + elapsedTime + " ms to calculate " + angleMaker.curveLength * 2 + " as pi.");
		System.out.println("Math.PI is " + Math.PI + ", and the difference is " + (Math.PI - angleMaker.curveLength * 2));
		System.out.println(Math.PI);
		System.out.println(angleMaker.curveLength * 2 /*+ " -"*/);
//		System.out.println("____________________________");
//		System.out.println(Math.PI - angleMaker.curveLength * 2);
	}
}
