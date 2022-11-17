-- MySQL Script generated by MySQL Workbench
-- Thu Nov 17 14:41:22 2022
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema qtea
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `qtea` ;

-- -----------------------------------------------------
-- Schema qtea
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `qtea` DEFAULT CHARACTER SET utf8 ;
-- -----------------------------------------------------
-- Schema qteaa
-- -----------------------------------------------------
USE `qtea` ;

-- -----------------------------------------------------
-- Table `qtea`.`Category`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `qtea`.`Category` ;

CREATE TABLE IF NOT EXISTS `qtea`.`Category` (
  `id` INT NOT NULL,
  `name` VARCHAR(45) NOT NULL,
  `parent` INT NULL,
  PRIMARY KEY (`id`),
  INDEX `a` (`id` DESC) VISIBLE,
  CONSTRAINT `category`
    FOREIGN KEY (`id`)
    REFERENCES `qtea`.`Category` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `qtea`.`Product`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `qtea`.`Product` ;

CREATE TABLE IF NOT EXISTS `qtea`.`Product` (
  `idProduct` INT NOT NULL,
  `Name` VARCHAR(225) NOT NULL,
  `Image` VARCHAR(255) NOT NULL,
  `Stock` INT NULL,
  `Category` INT NOT NULL,
  PRIMARY KEY (`idProduct`, `Image`),
  INDEX `category_idx` (`Category` ASC) VISIBLE,
  CONSTRAINT `categoryProduct`
    FOREIGN KEY (`Category`)
    REFERENCES `qtea`.`Category` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `qtea`.`Pricing`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `qtea`.`Pricing` ;

CREATE TABLE IF NOT EXISTS `qtea`.`Pricing` (
  `idPricing` INT NOT NULL,
  `ProductID` INT NOT NULL,
  `date_created` DATETIME NOT NULL,
  `date_expiry` DATETIME NOT NULL,
  `in_active` TINYINT NOT NULL,
  `BasePrice` VARCHAR(45) NULL,
  PRIMARY KEY (`idPricing`),
  INDEX `ProductID_idx` (`ProductID` ASC) VISIBLE,
  CONSTRAINT `ProductID`
    FOREIGN KEY (`ProductID`)
    REFERENCES `qtea`.`Product` (`idProduct`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `qtea`.`Order`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `qtea`.`Order` ;

CREATE TABLE IF NOT EXISTS `qtea`.`Order` (
  `OrderID` INT NOT NULL,
  `Total` INT NOT NULL,
  `Status` INT NOT NULL,
  `DatePlaceOrder` DATETIME NOT NULL,
  `DateComplete` DATETIME NOT NULL,
  `OrderAddress` VARCHAR(255) NOT NULL,
  PRIMARY KEY (`OrderID`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `qtea`.`OrderDetails`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `qtea`.`OrderDetails` ;

CREATE TABLE IF NOT EXISTS `qtea`.`OrderDetails` (
  `DetailsID` INT NOT NULL,
  `ProductID` INT NOT NULL,
  `Quantity` INT NOT NULL,
  `Order` INT NOT NULL,
  PRIMARY KEY (`DetailsID`),
  INDEX `order_idx` (`Order` ASC) VISIBLE,
  INDEX `product_idx` (`ProductID` ASC) VISIBLE,
  CONSTRAINT `order`
    FOREIGN KEY (`Order`)
    REFERENCES `qtea`.`Order` (`OrderID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `product`
    FOREIGN KEY (`ProductID`)
    REFERENCES `qtea`.`Product` (`idProduct`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `qtea`.`Product_Discount`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `qtea`.`Product_Discount` ;

CREATE TABLE IF NOT EXISTS `qtea`.`Product_Discount` (
  `id` INT NOT NULL,
  `ProductID` INT NOT NULL,
  `DiscountValue` DOUBLE NOT NULL,
  `DiscountUnit` VARCHAR(20) NOT NULL,
  `CreateDate` DATETIME NOT NULL,
  `From` DATETIME NOT NULL,
  `Until` DATETIME NOT NULL,
  `CouponCode` VARCHAR(10) NOT NULL,
  `MinimumOrderValue` DOUBLE NOT NULL,
  `is_redeem_allowed` TINYINT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `product_idx` (`ProductID` ASC) VISIBLE,
  CONSTRAINT `productDiscount`
    FOREIGN KEY (`ProductID`)
    REFERENCES `qtea`.`Product` (`idProduct`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;