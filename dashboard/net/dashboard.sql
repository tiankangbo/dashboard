/*
Navicat MySQL Data Transfer

Source Server         : 172.25.250.244
Source Server Version : 50544
Source Host           : 172.25.250.244:3306
Source Database       : dashboard

Target Server Type    : MYSQL
Target Server Version : 50544
File Encoding         : 65001

Date: 2017-04-21 17:30:11
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for nodes
-- ----------------------------
DROP TABLE IF EXISTS `nodes`;
CREATE TABLE `nodes` (
  `id` int(20) unsigned NOT NULL AUTO_INCREMENT,
  `nodename` varchar(50) NOT NULL,
  `ip` varchar(50) NOT NULL,
  `mem_stat` varchar(2) NOT NULL,
  `insert_time` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00' ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1 ROW_FORMAT=COMPACT;

-- ----------------------------
-- Table structure for offlinetidt
-- ----------------------------
DROP TABLE IF EXISTS `offlinetidt`;
CREATE TABLE `offlinetidt` (
  `id` int(20) unsigned NOT NULL AUTO_INCREMENT,
  `nodename` varchar(50) NOT NULL,
  `mem_total` int(20) NOT NULL,
  `mem_used` int(20) NOT NULL,
  `mem_free` int(20) NOT NULL,
  `swap_total` int(20) NOT NULL,
  `swap_used` int(20) NOT NULL,
  `swap_free` int(20) NOT NULL,
  `disk_total` int(20) NOT NULL,
  `disk_used` int(20) NOT NULL,
  `disk_free` int(20) NOT NULL,
  `disk1_total` int(20) NOT NULL,
  `disk1_used` int(20) NOT NULL,
  `disk1_free` int(20) NOT NULL,
  `insert_time` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00' ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=16058 DEFAULT CHARSET=latin1;

-- ----------------------------
-- Table structure for realtidt
-- ----------------------------
DROP TABLE IF EXISTS `realtidt`;
CREATE TABLE `realtidt` (
  `id` int(20) unsigned NOT NULL AUTO_INCREMENT,
  `nodename` varchar(255) NOT NULL,
  `cpu_usage` double(10,0) NOT NULL,
  `cpu_temp` int(10) NOT NULL,
  `net_up` int(50) NOT NULL,
  `net_down` int(50) NOT NULL,
  `disk_rs` int(50) NOT NULL,
  `disk_ws` int(50) NOT NULL,
  `disk_io` double(10,0) NOT NULL,
  `insert_time` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00' ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=32109 DEFAULT CHARSET=latin1;
