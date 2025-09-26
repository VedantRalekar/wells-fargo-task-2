package com.wellsfargo.counselor.entity;

import jakarta.persistence.*;
import java.time.Instant;
import java.util.*;


@Entity
@Table(name = "portfolios")
public class Portfolio {

    @Id
    @GeneratedValue(strategy = GenerationType.AUTO)
    private UUID id;

    private String name;
    private String description;
    private String currency;
    private boolean active = true;

    private Instant createdAt = Instant.now();
    private Instant updatedAt = Instant.now();

    @ManyToOne
    @JoinColumn(name = "client_id")
    private Client client;

    @OneToMany(mappedBy = "portfolio", cascade = CascadeType.ALL)
    private List<Holding> holdings = new ArrayList<>();

    // Constructors
    public Portfolio() {}
    public Portfolio(String name, String description, String currency, Client client) {
        this.name = name;
        this.description = description;
        this.currency = currency;
        this.client = client;
    }

    // Getters and setters
    public UUID getId() { return id; }
    public String getName() { return name; }
    public void setName(String name) { this.name = name; }
    public String getDescription() { return description; }
    public void setDescription(String description) { this.description = description; }
    public String getCurrency() { return currency; }
    public void setCurrency(String currency) { this.currency = currency; }
    public boolean isActive() { return active; }
    public void setActive(boolean active) { this.active = active; }
    public Client getClient() { return client; }
    public void setClient(Client client) { this.client = client; }
}
