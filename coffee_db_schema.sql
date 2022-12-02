CREATE SCHEMA IF NOT EXISTS `coffeeshopschema` DEFAULT CHARACTER SET utf8 ;
USE `coffeeshop` ;


CREATE TABLE IF NOT EXISTS `coffeeshop`.`Sales Outlets` (
  `sales_outlet_id` INT NOT NULL,
  `sales_outlet_type` VARCHAR(45) NULL,
  `store_square_feet` INT NULL,
  `store_address` VARCHAR(100) NULL,
  `store_city` VARCHAR(50) NULL,
  `store_state` VARCHAR(2) NULL,
  `store_telephone` CHAR(12) NULL,
  `store_postal_code` INT(5) NULL,
  `neighborhood` VARCHAR(100) NULL,
  PRIMARY KEY (`sales_outlet_id`))



CREATE TABLE IF NOT EXISTS `coffeeshop`.`Staff` (
  `staff_id` INT NOT NULL,
  `first_name` VARCHAR(50) NULL,
  `last_name` VARCHAR(50) NULL,
  `position` VARCHAR(50) NULL,
  `start_date` DATE NULL,
  `location` INT NULL,
  PRIMARY KEY (`staff_id`),
  INDEX `location_idx` (`location` ASC) VISIBLE,
  CONSTRAINT `location`
    FOREIGN KEY (`location`)
    REFERENCES `coffeeshop`.`Sales Outlets` (`sales_outlet_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)



CREATE TABLE IF NOT EXISTS `coffeeshop`.`Customer` (
  `customer_id` INT NOT NULL,
  `home_store` INT NULL,
  `customer_name` VARCHAR(100) NULL,
  `customer_email` VARCHAR(100) NULL,
  `customer_since` DATE NULL,
  `loyalty_card_number` VARCHAR(12) NULL,
  `birthdate` DATE NULL,
  `gender` VARCHAR(1) NULL,
  PRIMARY KEY (`customer_id`),
  UNIQUE INDEX `customer_email_UNIQUE` (`customer_email` ASC) VISIBLE,
  UNIQUE INDEX `loyalty_card_number_UNIQUE` (`loyalty_card_number` ASC) VISIBLE,
  INDEX `home_store_idx` (`home_store` ASC) VISIBLE,
  CONSTRAINT `home_store`
    FOREIGN KEY (`home_store`)
    REFERENCES `coffeeshop`.`Sales Outlets` (`sales_outlet_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)



CREATE TABLE IF NOT EXISTS `coffeeshop`.`Product Group` (
  `product_group_id` INT NOT NULL,
  `product_group` VARCHAR(50) NULL,
  PRIMARY KEY (`product_group_id`))



CREATE TABLE IF NOT EXISTS `coffeeshop`.`Product Category` (
  `product_category_id` INT NOT NULL,
  `product_category` VARCHAR(50) NULL,
  PRIMARY KEY (`product_category_id`))



CREATE TABLE IF NOT EXISTS `coffeeshop`.`Product Type` (
  `product_type_id` INT NOT NULL,
  `product_type` VARCHAR(50) NULL,
  PRIMARY KEY (`product_type_id`))



CREATE TABLE IF NOT EXISTS `coffeeshop`.`Product` (
  `product_id` INT NOT NULL,
  `product_group_id` INT NULL,
  `product_category_id` INT NULL,
  `product_type_id` INT NULL,
  `product` VARCHAR(100) NULL,
  `product_description` VARCHAR(200) NULL,
  `unit_of_measure` VARCHAR(45) NULL,
  `tax_exempt_yn` CHAR(1) NULL,
  `promo_yn` CHAR(1) NULL,
  `new_product_yn` CHAR(1) NULL,
  PRIMARY KEY (`product_id`),
  INDEX `product_group_id_idx` (`product_group_id` ASC) VISIBLE,
  INDEX `product_category_id_idx` (`product_category_id` ASC) VISIBLE,
  INDEX `product_type_id_idx` (`product_type_id` ASC) VISIBLE,
  CONSTRAINT `product_group_id`
    FOREIGN KEY (`product_group_id`)
    REFERENCES `coffeeshop`.`Product Group` (`product_group_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `product_category_id`
    FOREIGN KEY (`product_category_id`)
    REFERENCES `coffeeshop`.`Product Category` (`product_category_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `product_type_id`
    FOREIGN KEY (`product_type_id`)
    REFERENCES `coffeeshop`.`Product Type` (`product_type_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)


CREATE TABLE IF NOT EXISTS `coffeeshop`.`Pastry Inventory` (
  `sales_outlet_id` INT NOT NULL,
  `transaction_date` DATE NOT NULL,
  `product_id` INT NOT NULL,
  `start_of_day` INT NULL,
  `quantity_sold` INT NULL,
  PRIMARY KEY (`sales_outlet_id`, `transaction_date`, `product_id`),
  INDEX `product_id_idx` (`product_id` ASC) VISIBLE,
  CONSTRAINT `sales_outlet_id`
    FOREIGN KEY (`sales_outlet_id`)
    REFERENCES `coffeeshopdb`.`Sales Outlets` (`sales_outlet_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `product_id`
    FOREIGN KEY (`product_id`)
    REFERENCES `coffeeshop`.`Product` (`product_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)


CREATE TABLE IF NOT EXISTS `coffeeshopdb`.`Pricing` (
  `product_id` INT NOT NULL,
  `current_wholesale_price` DECIMAL(3,2) NULL,
  `current_retail_price` DECIMAL(3,2) NULL,
  PRIMARY KEY (`product_id`),
  CONSTRAINT `product_id`
    FOREIGN KEY (`product_id`)
    REFERENCES `coffeeshopdb`.`Product` (`product_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)



CREATE TABLE IF NOT EXISTS `coffeeshop`.`Transactions` (
  `transaction_id` INT NOT NULL,
  `transaction_date` DATE NOT NULL,
  `transaction_time` TIME NOT NULL,
  `sales_outlet_id` INT NOT NULL,
  `staff_id` INT NULL,
  `customer_id` INT NULL,
  `instore_yn` CHAR(1) NULL,
  `order` INT NULL,
  `line_item_id` INT NULL,
  `product_id` INT NULL,
  `quantity` INT NULL,
  `unit_price` DECIMAL(3,2) NULL,
  `promo_item_yn` CHAR(1) NULL,
  PRIMARY KEY (`transaction_id`, `transaction_date`, `transaction_time`, `sales_outlet_id`),
  INDEX `sales_outlet_id_idx` (`sales_outlet_id` ASC) VISIBLE,
  INDEX `staff_id_idx` (`staff_id` ASC) VISIBLE,
  INDEX `customer_id_idx` (`customer_id` ASC) VISIBLE,
  INDEX `product_id_idx` (`product_id` ASC) VISIBLE,
  CONSTRAINT `sales_outlet_id`
    FOREIGN KEY (`sales_outlet_id`)
    REFERENCES `coffeeshop`.`Sales Outlets` (`sales_outlet_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `staff_id`
    FOREIGN KEY (`staff_id`)
    REFERENCES `coffeeshop`.`Staff` (`staff_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `customer_id`
    FOREIGN KEY (`customer_id`)
    REFERENCES `coffeeshop`.`Customer` (`customer_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `product_id`
    FOREIGN KEY (`product_id`)
    REFERENCES `coffeeshop`.`Product` (`product_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)

