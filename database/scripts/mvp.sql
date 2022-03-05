
CREATE  TABLE wallets (
	wallet_address       varchar  NOT NULL,
	net_worth            money DEFAULT 0.0 NOT NULL,
	CONSTRAINT pk_wallet_address PRIMARY KEY (wallet_address)
);

CREATE  TABLE coins (
	coin_id              varchar  NOT NULL,
	coin_name            varchar  NOT NULL,
	coin_price           double precision  NOT NULL,
	CONSTRAINT pk_coin PRIMARY KEY (coin_id)
);

CREATE  TABLE chains (
	chain_id             varchar  NOT NULL,
	coin_id              varchar  NOT NULL,
	chain_name           varchar  NOT NULL,
	CONSTRAINT pk_chain_id PRIMARY KEY (chain_id),
	CONSTRAINT fk_coin_id  FOREIGN KEY (coin_id) REFERENCES coins(coin_id)
);

CREATE  TABLE price_tracking_platforms (
	ptp_id          varchar  NOT NULL,
	domain             varchar  NOT NULL,
	ip                   varchar(15)  NOT NULL,
	root_https           varchar  NOT NULL,
	CONSTRAINT pk_ptp_id PRIMARY KEY (ptp_id)
);

CREATE  TABLE crypto_tracking_platforms(
	ctp_id               varchar  NOT NULL,
	domain               varchar  NOT NULL,
	ip                   varchar(15)  NOT NULL,
	root_https           varchar  NOT NULL,
	CONSTRAINT pk_ctp_id PRIMARY KEY (ctp_id)
);

CREATE  TABLE scraped_tokens(
    uri                  varchar  NOT NULL UNIQUE,
    token_id             varchar  NOT NULL UNIQUE,
	ctp_id          varchar  NOT NULL,
	discovery_timestamp  timestamp  NOT NULL,
	listed_timestamp     timestamp  NOT NULL,
    CONSTRAINT pk_uri_token_id PRIMARY KEY (uri),
	CONSTRAINT fk_ctp_name_id FOREIGN KEY (ctp_id) REFERENCES crypto_tracking_platforms(ctp_id)
);

CREATE  TABLE tokens (
	token_contract       varchar  NOT NULL,
	chain_id             varchar  NOT NULL,
    token_id             varchar  NOT NULL UNIQUE,
    scraped_token        varchar  NOT NULL UNIQUE,
	total_supply         double precision,
	market_cap           double precision,
	launched_timestamp   timestamp,
	price_history        json  NOT NULL,
	token_name           varchar  NOT NULL,

	CONSTRAINT pk_token_contract PRIMARY KEY (token_contract),
	CONSTRAINT fk_chain_id FOREIGN KEY (chain_id) REFERENCES chains(chain_id),
	CONSTRAINT fk_scraped_token FOREIGN KEY (scraped_token) REFERENCES scraped_tokens(token_id)
);

CREATE  TABLE wallet_assets_coins (
	wallet_address       varchar  NOT NULL,
	coin_id              varchar  NOT NULL,
	quantity             double precision DEFAULT 0.0 NOT NULL,
	CONSTRAINT pk_wallet_assets_coins PRIMARY KEY (wallet_address, coin_id),
	CONSTRAINT fk_wallet_address FOREIGN KEY (wallet_address) REFERENCES wallets(wallet_address),
	CONSTRAINT fk_coin_id FOREIGN KEY (coin_id) REFERENCES coins(coin_id)
);

CREATE  TABLE wallet_assets_tokens (
	wallet_address       varchar  NOT NULL,
	token_contract       varchar  NOT NULL,
	quantity             double precision DEFAULT 0.0 NOT NULL,
	CONSTRAINT pk_wallet_assets_tokens PRIMARY KEY (wallet_address, token_contract),
	CONSTRAINT fk_wallet_address FOREIGN KEY (wallet_address) REFERENCES wallets(wallet_address),
	CONSTRAINT fk_token_contract FOREIGN KEY (token_contract) REFERENCES tokens(token_contract)
);

CREATE TABLE raw_discovered_token (
	token_id             varchar  NOT NULL,
	ctp_id               varchar  NOT NULL,
	url_path               varchar  NOT NULL,
	token_name           varchar  NOT NULL,
	discovery_timestamp  timestamp DEFAULT CURRENT_TIMESTAMP NOT NULL,
	chain_name           varchar(500)  NOT NULL,
	contract             varchar  NOT NULL,
	price                money    NOT NULL,
	listed_timestamp     timestamp NOT NULL,
	CONSTRAINT pk_raw_discovered_token PRIMARY KEY (token_id),
	CONSTRAINT fk_ctp_id FOREIGN KEY (ctp_id) REFERENCES crypto_tracking_platforms(ctp_id)
);

CREATE  TABLE price_tracked_tokens (
	token_contract       varchar  NOT NULL,
	ptp_id          varchar  NOT NULL,
	tracked_since        timestamp DEFAULT CURRENT_TIMESTAMP NOT NULL,
	last_update            timestamp DEFAULT CURRENT_TIMESTAMP NOT NULL,
	CONSTRAINT pk_tracked_tokens PRIMARY KEY (token_contract),
	CONSTRAINT fk_tracked_tokens FOREIGN KEY (token_contract) REFERENCES tokens(token_contract),
	CONSTRAINT fk_ptp_id FOREIGN KEY (ptp_id) REFERENCES price_tracking_platforms(ptp_id)
);

insert into crypto_tracking_platforms (ctp_id, domain, ip, root_https) VALUES ('coingecko', 'coingecko.com', '104.18.4.127', 'https://www.coingecko.com');
insert into crypto_tracking_platforms (ctp_id, domain, ip, root_https) VALUES ('coinbase', 'coinbase.com', '104.18.7.10', 'https://www.coinbase.com/');

select * from raw_discovered_token;
