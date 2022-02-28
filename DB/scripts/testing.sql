CREATE TYPE transaction_type AS ENUM ('buy',  'sell');

CREATE SEQUENCE order_id_sequence;

CREATE TABLE positions_delivery (
	order_id             integer  NOT NULL,
	wallet_address       varchar  NOT NULL,
	token_contract       varchar  NOT NULL,
	quantity_tokens      double precision  NOT NULL,
	timestamp_pd          timestamp DEFAULT CURRENT_TIMESTAMP,
	CONSTRAINT unq_order_id UNIQUE (order_id),
	CONSTRAINT pk_token_order PRIMARY KEY (order_id),
	CONSTRAINT fk_wallet_address FOREIGN KEY (wallet_address) REFERENCES wallets(wallet_address),
	CONSTRAINT fk_token_contract FOREIGN KEY (token_contract) REFERENCES price_tracked_tokens(token_contract)
);


CREATE  TABLE transactions (
	order_id             integer  NOT NULL,
	wallet_address       varchar  NOT NULL,
	fees_cost            double precision  NOT NULL,
	"timestamp"          timestamp DEFAULT CURRENT_TIMESTAMP,
	token_price          double precision,
	total_cost           double precision,
	transaction_type     transaction_type  NOT NULL,
	CONSTRAINT pk_tbl_4 PRIMARY KEY (order_id)
);


CREATE  TABLE active_positions (
	order_id             integer  NOT NULL,
	actived_timestamp    timestamp DEFAULT CURRENT_TIMESTAMP,
	CONSTRAINT pk_active_orders PRIMARY KEY (order_id)
);

CREATE  TABLE "position_status " (
	order_id             integer  NOT NULL,
	current_profit       double precision DEFAULT 0.0 NOT NULL,
	last_update          timestamp DEFAULT CURRENT_TIMESTAMP NOT NULL,
	order_value          double precision DEFAULT 0.0
);

CREATE  TABLE positions_order (
	order_id             integer  NOT NULL,
	wallet_address       varchar  NOT NULL,
	order_timestamp      timestamp DEFAULT CURRENT_TIMESTAMP,
	CONSTRAINT pk_asset_order PRIMARY KEY (order_id)
);
