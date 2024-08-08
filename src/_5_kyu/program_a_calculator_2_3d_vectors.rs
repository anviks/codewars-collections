/*
 * https://www.codewars.com/kata/58ee4962dc4f81d6f400001c
 */


// TODO: Complete the Task as specified in the Kata Description

#[derive(Copy, Clone, Debug)]
struct Vector {
    i: f64,
    j: f64,
    k: f64,
}

impl Vector {
    pub fn new(i: f64, j: f64, k: f64) -> Self {
        Vector {
            i,
            j,
            k,
        }
    }

    pub fn get_magnitude(&self) -> f64 {
        (self.i.powi(2) + self.j.powi(2) + self.k.powi(2)).sqrt()
    }

    pub fn get_i() -> Self {
        Self::new(1.0, 0.0, 0.0)
    }

    pub fn get_j() -> Self {
        Self::new(0.0, 1.0, 0.0)
    }

    pub fn get_k() -> Self {
        Self::new(0.0, 0.0, 1.0)
    }

    pub fn add(&self, other: Self) -> Self {
        Self::new(self.i + other.i, self.j + other.j, self.k + other.k)
    }

    pub fn multiply_by_scalar(&self, n: f64) -> Self {
        Self::new(self.i * n, self.j * n, self.k * n)
    }

    pub fn dot(&self, other: Self) -> f64 {
        self.i * other.i + self.j * other.j + self.k * other.k
    }

    pub fn cross(&self, other: Self) -> Self {
        Self::new(
            self.j * other.k - self.k * other.j,
            self.k * other.i - self.i * other.k,
            self.i * other.j - self.j * other.i,
        )
    }

    pub fn is_parallel_to(&self, other: Self) -> bool {
        if self.get_magnitude() == 0.0 || other.get_magnitude() == 0.0 {
            return false;
        }

        let cross_product = self.cross(other);
        is_close_to(cross_product.i, 0.0) && is_close_to(cross_product.j, 0.0) && is_close_to(cross_product.k, 0.0)
    }

    pub fn is_perpendicular_to(&self, other: Self) -> bool {
        if self.get_magnitude() == 0.0 || other.get_magnitude() == 0.0 {
            return false;
        }

        is_close_to(self.dot(other), 0.0)
    }

    pub fn normalize(&self) -> Self {
        let magnitude = self.get_magnitude();
        Self::new(self.i / magnitude, self.j / magnitude, self.k / magnitude)
    }

    pub fn is_normalized(&self) -> bool {
        let magnitude = self.get_magnitude();
        is_close_to(magnitude, 1.0)
    }
}

fn is_close_to(a: f64, b: f64) -> bool {
    (a - b).abs() < 0.000001
}


#[cfg(test)]
mod tests {
    use super::*;

    fn are_equals(a: f64, b: f64) -> bool {
        (a - b).abs() < 0.000001
    }

    #[test]
    fn constructor_test() {
        let v = Vector::new(1.0, 2.0, 3.0);
        assert_eq!(1.0, v.i, "Value of first argument passed into struct constructor should be assigned to \"i\"");
        assert_eq!(2.0, v.j, "Value of second argument passed into struct constructor should be assigned to \"j\"");
        assert_eq!(3.0, v.k, "Value of third argument passed into struct constructor should be assigned to \"k\"");

        let v = Vector::new(-4.0 / 3.0, 40.0 / 27.0, 68.0 / 69.0);
        assert!(are_equals(v.i, -4.0 / 3.0), "\"i\" of Vector should equal -4 / 3");
        assert!(are_equals(v.j, 40.0 / 27.0), "\"j\" of Vector should equal 40 / 27");
        assert!(are_equals(v.k, 68.0 / 69.0), "\"k\" of Vector should equal 68 / 69");
    }

    #[test]
    fn get_magnitude_test() {
        let v = Vector::new(6.0, 10.0, -3.0);
        assert!(are_equals(v.get_magnitude(), 145f64.sqrt()));
    }

    #[test]
    fn struct_methods_test() {
        let i = Vector::get_i();
        let j = Vector::get_j();
        let k = Vector::get_k();
        assert_eq!(1.0, i.i);
        assert_eq!(0.0, i.j);
        assert_eq!(0.0, i.k);
        assert_eq!(0.0, j.i);
        assert_eq!(1.0, j.j);
        assert_eq!(0.0, j.k);
        assert_eq!(0.0, k.i);
        assert_eq!(0.0, k.j);
        assert_eq!(1.0, k.k);
    }

    #[test]
    fn add_test() {
        let v = Vector::new(3.0, 7.0 / 2.0, -3.0 / 2.0);
        let s: Vector = v.add(Vector::new(-27.0, 3.0, 4.0));
        assert!(are_equals(s.i, -24.0));
        assert!(are_equals(s.j, 13.0 / 2.0));
        assert!(are_equals(s.k, 5.0 / 2.0));
    }

    #[test]
    fn multiply_test() {
        let v = Vector::new(1.0 / 3.0, 177.0 / 27.0, -99.0);
        let e = v.multiply_by_scalar(-3.0 / 7.0);
        assert!(are_equals(e.i, -1.0 / 7.0));
        assert!(are_equals(e.j, -59.0 / 21.0));
        assert!(are_equals(e.k, 297.0 / 7.0));
    }

    #[test]
    fn dot_test() {
        let v = Vector::new(-99.0 / 71.0, 22.0 / 23.0, 45.0);
        assert!(are_equals(v.dot(Vector::new(-5.0, 4.0, 7.0)), 325.7979179));
    }

    #[test]
    fn cross_test() {
        let a = Vector::new(2.0, 1.0, 3.0);
        let b = Vector::new(4.0, 6.0, 5.0);
        let a_cross_b = a.cross(b);
        let b_cross_a = b.cross(a);
        assert!(are_equals(a_cross_b.i, -13.0));
        assert!(are_equals(a_cross_b.j, 2.0));
        assert!(are_equals(a_cross_b.k, 8.0));
        assert!(are_equals(b_cross_a.i, 13.0));
        assert!(are_equals(b_cross_a.j, -2.0));
        assert!(are_equals(b_cross_a.k, -8.0));
    }

    #[test]
    fn parallel_test() {
        let a = Vector::new(1045.0 / 23.0, -666.0 / 37.0, 15.0);
        let b = Vector::new(161.3385037, -59124.0 / 925.0, 9854.0 / 185.0);
        assert!(a.is_parallel_to(b));
        assert!(b.is_parallel_to(a));
        let c = Vector::new(-3.0, 0.0, 5.0);
        let d = Vector::new(-12.0, 1.0, 20.0);
        assert!(!c.is_parallel_to(d));
        assert!(!d.is_parallel_to(c));
    }

    #[test]
    fn perpendicular_test() {
        let a = Vector::new(3.0, 4.0, 7.0);
        let b = Vector::new(1.0 / 3.0, 2.0, -9.0 / 7.0);
        assert!(a.is_perpendicular_to(b));
        assert!(b.is_perpendicular_to(a));
        let c = Vector::new(1.0, 3.0, 5.0);
        let d = Vector::new(-2.0, -7.0, 4.4);
        assert!(!c.is_perpendicular_to(d));
        assert!(!d.is_perpendicular_to(c));
    }

    #[test]
    fn normalize_test() {
        let v = Vector::new(-1.0, -1.0, 1.0);
        let u = v.normalize();
        assert!(are_equals(u.get_magnitude(), 1.0));
        assert!(are_equals(u.i, -1.0 / 3f64.sqrt()));
        assert!(are_equals(u.j, -1.0 / 3f64.sqrt()));
        assert!(are_equals(u.k, 1.0 / 3f64.sqrt()));
    }

    #[test]
    fn is_normalized_test() {
        let a = Vector::new(-1.0 / 2f64.sqrt(), 0.0, 1.0 / 2f64.sqrt());
        let b = Vector::new(1.0, 1.0, 1.0);
        assert!(a.is_normalized());
        assert!(!b.is_normalized());
    }
}
