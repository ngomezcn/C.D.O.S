CREATE TYPE "public".transaction_type AS ENUM ('buy',  'sell');

CREATE  TABLE "public"."assets delivery" ( 
 );

CREATE  TABLE "public".crypto_tracking_platforms ( 
	ctp_name_id          varchar(100)  NOT NULL  ,
	"domain"             varchar(100)  NOT NULL  ,
	ip                   varchar(9)  NOT NULL  ,
	root_https           varchar  NOT NULL  ,
	CONSTRAINT pk_crypto_tracking_platform PRIMARY KEY ( ctp_name_id )
 );

CREATE  TABLE "public".price_tracking_platforms ( 
	ptp_name_id          varchar(100)  NOT NULL  ,
	"domain"             varchar(100)  NOT NULL  ,
	ip                   varchar(12)  NOT NULL  ,
	root_https           varchar  NOT NULL  ,
	CONSTRAINT pk_crypto_tracking_platform_0 PRIMARY KEY ( ptp_name_id )
 );

CREATE  TABLE "public".raw_scraped_tokens ( 
	token_id             varchar  NOT NULL  ,
	ctp_name_id          varchar  NOT NULL  ,
	token_name           varchar(100)  NOT NULL  ,
	discovery_timestamp  timestamp(12) DEFAULT CURRENT_TIMESTAMP NOT NULL  ,
	chain_name           varchar  NOT NULL  ,
	listed_timestamp     timestamp(12) DEFAULT CURRENT_TIMESTAMP NOT NULL  ,
	uri                  varchar    ,
	CONSTRAINT pk_new_tokens_discovered PRIMARY KEY ( token_id ),
	CONSTRAINT fk_raw_scraped_tokens FOREIGN KEY ( ctp_name_id ) REFERENCES "public".crypto_tracking_platforms( ctp_name_id )   
 );

CREATE  TABLE "public".scrapy_tokens ( 
	listed_timestamp     timestamp(12)  NOT NULL  ,
	discovered_timestamp timestamp(12)  NOT NULL  ,
	ptp_name_id          varchar  NOT NULL  ,
	ctp_name_id          varchar  NOT NULL  ,
	CONSTRAINT fk_ptp_name_id FOREIGN KEY ( ptp_name_id ) REFERENCES "public".price_tracking_platforms( ptp_name_id )   ,
	CONSTRAINT fk_ctp_name_id FOREIGN KEY ( ctp_name_id ) REFERENCES "public".crypto_tracking_platforms( ctp_name_id )   
 );

CREATE  TABLE "public".wallets ( 
	wallet_address       varchar(44)  NOT NULL  ,
	net_worth            double precision DEFAULT 0.0 NOT NULL  ,
	CONSTRAINT pk_wallet PRIMARY KEY ( wallet_address )
 );

CREATE  TABLE "public".active_positions ( 
	order_id             integer  NOT NULL  ,
	actived_timestamp    timestamp(12) DEFAULT CURRENT_TIMESTAMP   ,
	CONSTRAINT pk_active_orders PRIMARY KEY ( order_id )
 );

CREATE  TABLE "public".chains ( 
	chain_id             varchar(100)  NOT NULL  ,
	chain_name           varchar(100)  NOT NULL  ,
	fk_coin_id           varchar  NOT NULL  ,
	CONSTRAINT pk_tbl PRIMARY KEY ( chain_id )
 );

CREATE  TABLE "public".coins ( 
	coin_id              varchar(100)  NOT NULL  ,
	fk_chain_id          varchar    ,
	coin_name            varchar(100)  NOT NULL  ,
	coin_price           double precision  NOT NULL  ,
	CONSTRAINT pk_coin PRIMARY KEY ( coin_id )
 );

CREATE  TABLE "public"."position_status " ( 
	order_id             integer  NOT NULL  ,
	current_profit       double precision DEFAULT 0.0 NOT NULL  ,
	last_update          timestamp DEFAULT CURRENT_TIMESTAMP NOT NULL  ,
	order_value          double precision DEFAULT 0.0   
 );

CREATE  TABLE "public".positions_delivery ( 
	order_id             integer  NOT NULL  ,
	wallet_address       varchar(100)  NOT NULL  ,
	token_contract       varchar  NOT NULL  ,
	quantity_tokens      double precision  NOT NULL  ,
	"timestamp"          timestamp(12) DEFAULT CURRENT_TIMESTAMP   ,
	CONSTRAINT unq_token_order_order_id UNIQUE ( order_id ) ,
	CONSTRAINT pk_token_order PRIMARY KEY ( order_id )
 );

CREATE  TABLE "public".positions_order ( 
	order_id             integer  NOT NULL  ,
	wallet_address       varchar(100)  NOT NULL  ,
	order_timestamp      timestamp(12) DEFAULT CURRENT_TIMESTAMP   ,
	CONSTRAINT pk_asset_order PRIMARY KEY ( order_id )
 );

CREATE  TABLE "public".tokens ( 
	token_contract       varchar(42)  NOT NULL  ,
	fk_chain_id          varchar  NOT NULL  ,
	token_id             varchar(100)  NOT NULL  ,
	total_suppy          bigint    ,
	market_cap           double precision    ,
	launched_timestamp   timestamp(12)    ,
	price_history        json  NOT NULL  ,
	token_name           varchar(100)  NOT NULL  ,
	listed_timestamp     timestamp(12)  NOT NULL  ,
	CONSTRAINT pk_token PRIMARY KEY ( token_contract )
 );

CREATE  TABLE "public".tracked_tokens ( 
	token_contract       varchar(42)  NOT NULL  ,
	ptp_name_id          varchar  NOT NULL  ,
	tracked_since        timestamp DEFAULT CURRENT_TIMESTAMP NOT NULL  ,
	last_updated         timestamp DEFAULT CURRENT_TIMESTAMP NOT NULL  ,
	CONSTRAINT pk_tracked_tokens PRIMARY KEY ( token_contract )
 );

CREATE  TABLE "public".transactions ( 
	order_id             integer  NOT NULL  ,
	wallet_address       varchar(100)  NOT NULL  ,
	fees_cost            double precision  NOT NULL  ,
	"timestamp"          timestamp(12) DEFAULT CURRENT_TIMESTAMP   ,
	token_price          double precision    ,
	total_cost           double precision    ,
	transaction_type     "public".transaction_type  NOT NULL  ,
	CONSTRAINT pk_tbl_4 PRIMARY KEY ( order_id )
 );

CREATE  TABLE "public".wallet_coins ( 
	wallet_address       varchar(44)  NOT NULL  ,
	coin_id              varchar(100)  NOT NULL  ,
	quantity             double precision DEFAULT 0.0 NOT NULL  
 );

CREATE  TABLE "public".wallet_tokens ( 
	wallet_address       varchar(44)  NOT NULL  ,
	token_contract       varchar(100)  NOT NULL  ,
	quantity             double precision DEFAULT 0.0 NOT NULL  
 );

ALTER TABLE "public".active_positions ADD CONSTRAINT fk_active_orders_token_order FOREIGN KEY ( order_id ) REFERENCES "public".positions_delivery( order_id );

ALTER TABLE "public".chains ADD CONSTRAINT fk_coin_id FOREIGN KEY ( fk_coin_id ) REFERENCES "public".coins( coin_id );

ALTER TABLE "public".coins ADD CONSTRAINT fk_chain_id FOREIGN KEY ( fk_chain_id ) REFERENCES "public".chains( chain_id );

ALTER TABLE "public"."position_status " ADD CONSTRAINT fk_order_id FOREIGN KEY ( order_id ) REFERENCES "public".active_positions( order_id );

ALTER TABLE "public".positions_delivery ADD CONSTRAINT fk_token_contract FOREIGN KEY ( token_contract ) REFERENCES "public".tracked_tokens( token_contract );

ALTER TABLE "public".positions_delivery ADD CONSTRAINT fk_wallet_address FOREIGN KEY ( wallet_address ) REFERENCES "public".wallets( wallet_address );

ALTER TABLE "public".positions_order ADD CONSTRAINT fk_wallet_address FOREIGN KEY ( wallet_address ) REFERENCES "public".wallets( wallet_address );

ALTER TABLE "public".positions_order ADD CONSTRAINT fk_order_id FOREIGN KEY ( order_id ) REFERENCES "public".positions_delivery( order_id );

ALTER TABLE "public".tokens ADD CONSTRAINT fk_chain_id FOREIGN KEY ( fk_chain_id ) REFERENCES "public".chains( chain_id );

ALTER TABLE "public".tracked_tokens ADD CONSTRAINT fk_token_contract FOREIGN KEY ( token_contract ) REFERENCES "public".tokens( token_contract );

ALTER TABLE "public".tracked_tokens ADD CONSTRAINT fk_price_tracking_platform_id FOREIGN KEY ( ptp_name_id ) REFERENCES "public".price_tracking_platforms( ptp_name_id );

ALTER TABLE "public".transactions ADD CONSTRAINT fk_order_id FOREIGN KEY ( order_id ) REFERENCES "public".positions_delivery( order_id );

ALTER TABLE "public".transactions ADD CONSTRAINT fk_wallet_address FOREIGN KEY ( wallet_address ) REFERENCES "public".wallets( wallet_address );

ALTER TABLE "public".wallet_coins ADD CONSTRAINT fk_wallet_address_0 FOREIGN KEY ( wallet_address ) REFERENCES "public".wallets( wallet_address );

ALTER TABLE "public".wallet_coins ADD CONSTRAINT fk_coin_id FOREIGN KEY ( coin_id ) REFERENCES "public".coins( coin_id );

ALTER TABLE "public".wallet_tokens ADD CONSTRAINT fk_token_contract FOREIGN KEY ( token_contract ) REFERENCES "public".tokens( token_contract );

ALTER TABLE "public".wallet_tokens ADD CONSTRAINT fk_wallet_address FOREIGN KEY ( wallet_address ) REFERENCES "public".wallets( wallet_address );

