// I have a lot of methods here for the sake of completeness even though they aren't needed

public class Vector2 {
	
	public double x;
	public double y;
	
	public Vector2() {}
	
	public Vector2(double x, double y) {
		this.x = x;
		this.y = y;
	}
	
	public Vector2(Vector2 v) {
		this.x = v.x;
		this.y = v.y;
	}
	
	public Vector2 add(Vector2 v) {
		return new Vector2(x + v.x, y + v.y);
	}
	
	public Vector2 sub(Vector2 v) {
		return new Vector2(x - v.x, y - v.y);
	}
	
	public Vector2 mul(double v) {
		return new Vector2(x * v, y * v);
	}
	
	public Vector2 div(double v) {
		return new Vector2(x / v, y / v);
	}
	
	public Vector2 mul(Vector2 v) {
		return new Vector2(x * v.x, y * v.y);
	}
	
	public Vector2 div(Vector2 v) {
		return new Vector2(x / v.x, y / v.y);
	}
	
	public double length() {
		return Math.sqrt(x * x + y * y);
	}
	
	public double lengthSquared() {
		return x * x + y * y;
	}
	
	public Vector2 averageWith(Vector2 v) {
		return new Vector2((x+v.x)/2, (y+v.y)/2);
	}
	
	public Vector2 normalized() {
		double length = length();
		if (length == 0) {
			return new Vector2();
		}
		return new Vector2(x / length, y / length);
	}
	
	public Vector2 round() {
		return new Vector2(Math.round(x), Math.round(y));
	}
	
	public double distanceTo(Vector2 other){
		return sub(other).length();
	}
	
	public static Vector2 abs(Vector2 v) {
		return new Vector2(Math.abs(v.x), Math.abs(v.y));
	}
	
	@Override
	public String toString() {
		return "(" + x + ", " + y + ")";
	}
	
	@Override
	public boolean equals(Object obj) {
		if (!(obj instanceof Vector2 v)) { // you can declare variables like this (cool)
			return false;
		}
		return x == v.x && y == v.y;
	}
	
	// The docs (somewhere, i forgot where) say that if you override Object.equals() you should override Object.hashCode()
	@Override
	public int hashCode() {
		int result = Double.hashCode(x);
		result = 31 * result + Double.hashCode(y); // Apparently 31 is a convention for uniquer hashcodes
		return result;
	}
	
	public boolean equalsApprox(Vector2 v, double epsilon) {
		Vector2 difference = abs(sub(v));
		if (difference.x > epsilon){
			return false;
		} else {
			return !(difference.y > epsilon);
		}
	}
	
	public boolean equalsApprox(Vector2 v) {
		return equalsApprox(v, 1e-7); // default epsilon
	}
}
