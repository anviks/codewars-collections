/*
 * https://www.codewars.com/kata/58ee4962dc4f81d6f400001c
 */

#[derive(Copy, Clone, Debug)]
pub struct Vector {
    pub i: f64,
    pub j: f64,
    pub k: f64,
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
