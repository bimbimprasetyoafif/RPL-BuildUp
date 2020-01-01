package com.example.buildup.data;

import com.google.gson.annotations.Expose;
import com.google.gson.annotations.SerializedName;

public class AllRAB {
    @SerializedName("RABId")
    @Expose
    private Integer rABId;
    @SerializedName("WorkName")
    @Expose
    private String workName;
    @SerializedName("PriceTotal")
    @Expose
    private Integer priceTotal;
    @SerializedName("DesignId")
    @Expose
    private Integer designId;

    public Integer getrABId() {
        return rABId;
    }

    public void setrABId(Integer rABId) {
        this.rABId = rABId;
    }

    public String getWorkName() {
        return workName;
    }

    public void setWorkName(String workName) {
        this.workName = workName;
    }

    public Integer getPriceTotal() {
        return priceTotal;
    }

    public void setPriceTotal(Integer priceTotal) {
        this.priceTotal = priceTotal;
    }

    public Integer getDesignId() {
        return designId;
    }

    public void setDesignId(Integer designId) {
        this.designId = designId;
    }
}
